content = open("apps/registry/templates/registry/budget_calculator.html", "r", encoding="utf-8").read()

# Hero-ийн дараа chat section нэмэх
old = '<div class="page">'
new = '''<div class="chat-section">
  <div class="chat-wrap">
    <div class="chat-header">
      <div class="chat-title">🤖 Барилгын AI Зөвлөгөө</div>
      <div class="chat-sub">Барилгатай холбоотой асуултаа асуугаарай</div>
    </div>
    <div class="chat-messages" id="chat-messages">
      <div class="msg ai">
        <div class="msg-avatar">🤖</div>
        <div class="msg-bubble">Сайн байна уу! Би барилгын мэргэжилтэн AI. Барилга барихтай холбоотой асуулт байвал асуугаарай.<br><br>
        Жишээ асуултууд:<br>
        • Зөвшөөрөл яаж авах вэ?<br>
        • Барилгын компани яаж сонгох вэ?<br>
        • Хэдэн давхар барих нь зөв вэ?<br>
        • Монголд ямар барилгын материал сайн вэ?</div>
      </div>
    </div>
    <div class="chat-input-wrap">
      <input type="text" id="chat-input" class="chat-input" placeholder="Асуултаа бичнэ үү..." onkeydown="if(event.key==='Enter') sendChat()">
      <button class="chat-send" onclick="sendChat()">➤</button>
    </div>
  </div>
</div>

<div class="page">'''

if old in content:
    content = content.replace(old, new, 1)
    print("OK — chat UI нэмэгдлээ")
else:
    print("NOT FOUND")

# CSS нэмэх
old_css = '@media(max-width:900px)'
new_css = '''.chat-section{background:#f8fafc;border-bottom:0.5px solid #e2e8f0;padding:20px;}
    .chat-wrap{max-width:1100px;margin:0 auto;padding:0 20px;}
    .chat-header{margin-bottom:14px;}
    .chat-title{font-size:16px;font-weight:700;color:#1e293b;}
    .chat-sub{font-size:12px;color:#64748b;margin-top:3px;}
    .chat-messages{background:#fff;border:0.5px solid #e2e8f0;border-radius:12px;padding:16px;min-height:120px;max-height:320px;overflow-y:auto;display:flex;flex-direction:column;gap:12px;margin-bottom:10px;}
    .msg{display:flex;gap:10px;align-items:flex-start;}
    .msg.user{flex-direction:row-reverse;}
    .msg-avatar{width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0;background:#f1f5f9;}
    .msg.user .msg-avatar{background:#fef3c7;}
    .msg-bubble{background:#f8fafc;border:0.5px solid #e2e8f0;border-radius:12px;padding:10px 14px;font-size:13px;line-height:1.6;color:#1e293b;max-width:80%;}
    .msg.user .msg-bubble{background:#fef3c7;border-color:#f59e0b;}
    .msg.ai .msg-bubble{background:#fff;}
    .typing .msg-bubble{color:#94a3b8;font-style:italic;}
    .chat-input-wrap{display:flex;gap:8px;}
    .chat-input{flex:1;padding:10px 14px;border:1px solid #e2e8f0;border-radius:8px;font-size:13px;outline:none;}
    .chat-input:focus{border-color:#f59e0b;}
    .chat-send{padding:10px 18px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:8px;font-size:16px;cursor:pointer;font-weight:700;}
    .chat-send:hover{background:#e08c00;}
    @media(max-width:900px)'''

content = content.replace('@media(max-width:900px)', new_css, 1)

# JS нэмэх
old_js = 'document.getElementById("calc-form").addEventListener("submit"'
new_js = '''const chatHistory = [];

async function sendChat() {
  const input = document.getElementById("chat-input");
  const msg = input.value.trim();
  if (!msg) return;

  input.value = "";
  addMsg("user", msg);
  chatHistory.push({role: "user", content: msg});

  // Typing indicator
  const typingId = "typing-" + Date.now();
  addMsg("ai", "Бодож байна...", typingId, true);

  try {
    const res = await fetch("/budget/chat/", {
      method: "POST",
      headers: {"Content-Type": "application/json", "X-CSRFToken": getCookie("csrftoken")},
      body: JSON.stringify({message: msg, messages: chatHistory.slice(-10)})
    });
    const data = await res.json();
    removeMsg(typingId);
    if (data.reply) {
      addMsg("ai", data.reply);
      chatHistory.push({role: "assistant", content: data.reply});
    } else {
      addMsg("ai", "Алдаа гарлаа: " + (data.error || "Дахин оролдоно уу"));
    }
  } catch(e) {
    removeMsg(typingId);
    addMsg("ai", "Сервертэй холбогдоход алдаа гарлаа.");
  }
}

function addMsg(role, text, id, isTyping) {
  const wrap = document.getElementById("chat-messages");
  const div = document.createElement("div");
  div.className = "msg " + role + (isTyping ? " typing" : "");
  if (id) div.id = id;
  div.innerHTML = `<div class="msg-avatar">${role === "user" ? "👤" : "🤖"}</div><div class="msg-bubble">${text.replace(/\\n/g, "<br>")}</div>`;
  wrap.appendChild(div);
  wrap.scrollTop = wrap.scrollHeight;
}

function removeMsg(id) {
  const el = document.getElementById(id);
  if (el) el.remove();
}

function getCookie(name) {
  const v = document.cookie.match("(^|;) ?" + name + "=([^;]*)(;|$)");
  return v ? v[2] : null;
}

document.getElementById("calc-form").addEventListener("submit"'''

content = content.replace(old_js, new_js, 1)
open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8").write(content)
print("OK — JS нэмэгдлээ")