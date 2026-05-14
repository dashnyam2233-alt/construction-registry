# registry/messaging.py
"""
Нэгдсэн мессеж илгээх сервис.
Тохиргоог SiteConfig model-оос уншдаг — admin-аас өөрчилж болно.
"""
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests

logger = logging.getLogger(__name__)


def _get_config():
    """SiteConfig-г lazy import-оор авна"""
    from apps.messaging.models import SiteConfig
    return SiteConfig.get()


# ─────────────────────────────────────────
# EMAIL
# ─────────────────────────────────────────
def send_email(to_email: str, subject: str, body: str) -> dict:
    if not to_email or "@" not in to_email:
        return {"ok": False, "error": "Email хаяг буруу"}
    try:
        cfg = _get_config()
        if not cfg.email_host_user or not cfg.email_host_password:
            return {"ok": False, "error": "Email тохиргоо хийгдээгүй (Admin → Системийн тохиргоо)"}

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject or "(гарчиггүй)"
        msg["From"] = f"{cfg.sender_name} <{cfg.email_host_user}>"
        msg["To"] = to_email
        msg.attach(MIMEText(body, "plain", "utf-8"))

        with smtplib.SMTP(cfg.email_host, cfg.email_port) as server:
            if cfg.email_use_tls:
                server.starttls()
            server.login(cfg.email_host_user, cfg.email_host_password)
            server.sendmail(cfg.email_host_user, to_email, msg.as_string())

        return {"ok": True}
    except Exception as e:
        logger.error(f"Email алдаа [{to_email}]: {e}")
        return {"ok": False, "error": str(e)}


# ─────────────────────────────────────────
# SMS
# ─────────────────────────────────────────
def send_sms(phone: str, body: str) -> dict:
    phone = (phone or "").strip().replace("-", "").replace(" ", "")
    if not phone:
        return {"ok": False, "error": "Утасны дугаар хоосон"}
    try:
        cfg = _get_config()
        if not cfg.sms_gateway_url or not cfg.sms_gateway_token:
            return {"ok": False, "error": "SMS gateway тохируулаагүй (Admin → Системийн тохиргоо)"}

        resp = requests.post(
            cfg.sms_gateway_url,
            json={"phone": phone, "message": body, "sender": cfg.sms_sender_name},
            headers={"Authorization": f"Bearer {cfg.sms_gateway_token}"},
            timeout=10,
        )
        if resp.status_code == 200:
            return {"ok": True}
        return {"ok": False, "error": f"Gateway хариу: {resp.status_code} {resp.text[:200]}"}
    except Exception as e:
        logger.error(f"SMS алдаа [{phone}]: {e}")
        return {"ok": False, "error": str(e)}


# ─────────────────────────────────────────
# TELEGRAM
# ─────────────────────────────────────────
def send_telegram(chat_id: str, body: str) -> dict:
    chat_id = (chat_id or "").strip()
    if not chat_id:
        return {"ok": False, "error": "Telegram chat_id хоосон"}
    try:
        cfg = _get_config()
        token = cfg.telegram_bot_token
        if not token:
            return {"ok": False, "error": "Telegram Bot Token тохируулаагүй (Admin → Системийн тохиргоо)"}

        resp = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat_id, "text": body, "parse_mode": "HTML"},
            timeout=10,
        )
        data = resp.json()
        if data.get("ok"):
            return {"ok": True}
        return {"ok": False, "error": data.get("description", "Telegram алдаа")}
    except Exception as e:
        logger.error(f"Telegram алдаа [{chat_id}]: {e}")
        return {"ok": False, "error": str(e)}


# ─────────────────────────────────────────
# FACEBOOK MESSENGER
# ─────────────────────────────────────────
def send_facebook(psid: str, body: str) -> dict:
    psid = (psid or "").strip()
    if not psid:
        return {"ok": False, "error": "Facebook PSID хоосон"}
    try:
        cfg = _get_config()
        token = cfg.facebook_page_token
        if not token:
            return {"ok": False, "error": "Facebook Page Token тохируулаагүй (Admin → Системийн тохиргоо)"}

        resp = requests.post(
            "https://graph.facebook.com/v18.0/me/messages",
            params={"access_token": token},
            json={"recipient": {"id": psid}, "message": {"text": body}},
            timeout=10,
        )
        data = resp.json()
        if "error" not in data:
            return {"ok": True}
        return {"ok": False, "error": data["error"].get("message", "Facebook алдаа")}
    except Exception as e:
        logger.error(f"Facebook алдаа [{psid}]: {e}")
        return {"ok": False, "error": str(e)}


# ─────────────────────────────────────────
# VIBER
# ─────────────────────────────────────────
def send_viber(viber_id: str, body: str) -> dict:
    viber_id = (viber_id or "").strip()
    if not viber_id:
        return {"ok": False, "error": "Viber ID хоосон"}
    try:
        cfg = _get_config()
        token = cfg.viber_auth_token
        if not token:
            return {"ok": False, "error": "Viber Auth Token тохируулаагүй (Admin → Системийн тохиргоо)"}

        resp = requests.post(
            "https://chatapi.viber.com/pa/send_message",
            headers={"X-Viber-Auth-Token": token},
            json={"receiver": viber_id, "type": "text", "text": body},
            timeout=10,
        )
        data = resp.json()
        if data.get("status") == 0:
            return {"ok": True}
        return {"ok": False, "error": data.get("status_message", "Viber алдаа")}
    except Exception as e:
        logger.error(f"Viber алдаа [{viber_id}]: {e}")
        return {"ok": False, "error": str(e)}


# ─────────────────────────────────────────
# НЭГДСЭН ИЛГЭЭГЧ
# ─────────────────────────────────────────
CHANNEL_DISPATCH = {
    "email":    send_email,
    "sms":      send_sms,
    "telegram": send_telegram,
    "facebook": send_facebook,
    "viber":    send_viber,
}

CHANNEL_LABELS = {
    "email":    "✉️ Email",
    "sms":      "📱 SMS (Утас)",
    "telegram": "✈️ Telegram",
    "facebook": "📘 Facebook Messenger",
    "viber":    "💬 Viber",
}


def send_message(channel: str, recipient: str, subject: str, body: str) -> dict:
    fn = CHANNEL_DISPATCH.get(channel)
    if not fn:
        return {"ok": False, "error": f"Тодорхойгүй суваг: {channel}"}
    if channel == "email":
        return fn(recipient, subject, body)
    return fn(recipient, body)
