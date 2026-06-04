import os

# Global floating chat HTML + CSS + JS
chat_widget = """
<!-- AI Зөвлөх Widget -->
<style>
.ai-fab{position:fixed;bottom:24px;right:24px;z-index:9999;display:flex;flex-direction:column;align-items:flex-end;gap:10px;}
.ai-fab-btn{display:flex;align-items:center;gap:8px;padding:12px 18px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:50px;font-size:13px;font-weight:700;cursor:pointer;box-shadow:0 4px 16px rgba(0,0,0,0.2);transition:all 0.2s;}
.ai-fab-btn:hover{background:#e08c00;transform:scale(1.04);}
.ai-fab-btn .ai-ic{width:28px;height:28px;background:#1e3a4a;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#f59e0b;font-size:14px;font-weight:700;flex-shrink:0;}
.ai-chat-box{position:fixed;bottom:80px;right:24px;width:360px;background:#fff;border:0.5px solid #e2e8f0;border-radius:16px;box-shadow:0 8px 40px rgba(0,0,0,0.15);z-index:9999;display:none;flex-direction:column;overflow:hidden;max-height:520px;}
.ai-chat-box.open{display:flex;}
.ai-chat-hd{background:#1e3a4a;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;flex-shrink:0;}
.ai-chat-hd-left{display:flex;align-items:center;gap:10px;}
.ai-chat-hd-ic{width:36px;height:36px;background:#f59e0b;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:700;color:#1e3a4a;flex-shrink:0;}
.ai-chat-hd-t{color:#fff;font-size:14px;font-weight:700;}
.ai-chat-hd-s{color:#94a3b8;font-size:11px;margin-top:2px;}
.ai-chat-close{color:#94a3b8;background:none;border:none;font-size:20px;cursor:pointer;line-height:1;padding:0;}
.ai-chat-close:hover{color:#fff;}
.ai-chat-msgs{padding:14px;overflow-y:auto;flex:1;display:flex;flex-direction:column;gap:10px;background:#f8fafc;}
.ai-msg{display:flex;gap:8px;align-items:flex-start;}
.ai-msg.user{flex-direction:row-reverse;}
.ai-msg-av{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0;background:#e2e8f0;color:#1e293b;}
.ai-msg.user .ai-msg-av{background:#fef3c7;color:#854d0e;}
.ai-msg-bbl{border-radius:12px;padding:8px 12px;font-size:12px;line-height:1.6;color:#1e293b;max-width:85%;}
.ai-msg.ai .ai-msg-bbl{background:#fff;border:0.5px solid #e2e8f0;}
.ai-msg.user .ai-msg-bbl{background:#fef3c7;border:0.5px solid #f59e0b;}
.ai-msg.typing .ai-msg-bbl{color:#94a3b8;font-style:italic;}
.ai-chat-inp-wrap{padding:10px;border-top:0.5px solid #e2e8f0;display:flex;gap:6px;background:#fff;flex-shrink:0;}
.ai-chat-inp{flex:1;padding:8px 12px;border:1px solid #e2e8f0;border-radius:8px;font-size:12px;outline:none;font-family:inherit;}
.ai-chat-inp:focus{border-color:#f59e0b;}
.ai-chat-send{padding:8px 14px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:8px;font-size:13px;cursor:pointer;font-weight:700;}
.ai-chat-send:hover{background:#e08c00;}
@media(max-width:480px){.ai-chat-box{width:calc(100vw - 20px);right:10px;bottom:70px;}.ai-fab-btn span.ai-label{display:none;}}
</style>

<div class="ai-fab">
  <div class="ai-chat-box" id="ai-chat-box">
    <div class="ai-chat-hd">
      <div class="ai-chat-hd-left">
        <div class="ai-chat-hd-ic">AI</div>
        <div>
          <div class="ai-chat-hd-t">AI Зөвлөх</div>
          <div class="ai-chat-hd-s">Барилгын мэргэжилтэн</div>
        </div>
      </div>
      <button class="ai-chat-close" onclick="aiToggleChat()">✕</button>
    </div>
    <div class="ai-chat-msgs" id="ai-chat-msgs">
      <div class="ai-msg ai">
        <div class="ai-msg-av">AI</div>
        <div class="ai-msg-bbl">Сайн байна уу! Би барилгын мэргэжилтэн AI зөвлөх.<br><br>
        Дараах зүйлсийг тусална:<br>
        • Барилгын зөвшөөрөл, бүртгэл<br>
        • Материал сонгох зөвлөгөө<br>
        • Барилгын компани сонгох<br>
        • Төсөв, хугацааны тооцоо<br>
        • Барилгын норм, дүрэм</div>
      </div>
    </div>
    <div class="ai-chat-inp-wrap">
      <input type="text" id="ai-chat-inp" class="ai-chat-inp" placeholder="Асуултаа бичнэ үү..." onkeydown="if(event.key==='Enter') aiSendChat()">
      <button class="ai-chat-send" onclick="aiSendChat()">Илгээх</button>
    </div>
  </div>
  <button class="ai-fab-btn" onclick="aiToggleChat()" id="ai-fab-btn">
    <div class="ai-ic">AI</div>
    <span class="ai-label">AI Зөвлөх</span>
  </button>
</div>

<script>
const aiChatHistory = [];
let aiChatOpen = false;

function aiToggleChat() {
  aiChatOpen = !aiChatOpen;
  const box = document.getElementById("ai-chat-box");
  const btn = document.getElementById("ai-fab-btn");
  if (aiChatOpen) {
    box.classList.add("open");
    btn.innerHTML = '<div class="ai-ic">✕</div><span class="ai-label">Хаах</span>';
    document.getElementById("ai-chat-inp").focus();
  } else {
    box.classList.remove("open");
    btn.innerHTML = '<div class="ai-ic">AI</div><span class="ai-label">AI Зөвлөх</span>';
  }
}

async function aiSendChat() {
  const inp = document.getElementById("ai-chat-inp");
  const msg = inp.value.trim();
  if (!msg) return;
  inp.value = "";
  aiAddMsg("user", msg);
  aiChatHistory.push({role: "user", content: msg});
  const tid = "typing-" + Date.now();
  aiAddMsg("ai", "Бодож байна...", tid, true);
  try {
    const res = await fetch("/budget/chat/", {
      method: "POST",
      headers: {"Content-Type": "application/json", "X-CSRFToken": aiGetCookie("csrftoken")},
      body: JSON.stringify({message: msg, messages: aiChatHistory.slice(-10)})
    });
    const data = await res.json();
    aiRemoveMsg(tid);
    if (data.reply) {
      aiAddMsg("ai", data.reply);
      aiChatHistory.push({role: "assistant", content: data.reply});
    } else {
      aiAddMsg("ai", "Алдаа гарлаа. Дахин оролдоно уу.");
    }
  } catch(e) {
    aiRemoveMsg(tid);
    aiAddMsg("ai", "Холболтын алдаа гарлаа.");
  }
}

function aiAddMsg(role, text, id, isTyping) {
  const wrap = document.getElementById("ai-chat-msgs");
  const div = document.createElement("div");
  div.className = "ai-msg " + role + (isTyping ? " typing" : "");
  if (id) div.id = id;
  div.innerHTML = '<div class="ai-msg-av">' + (role === "user" ? "Та" : "AI") + '</div><div class="ai-msg-bbl">' + text.replace(/\\n/g, "<br>") + '</div>';
  wrap.appendChild(div);
  wrap.scrollTop = wrap.scrollHeight;
}

function aiRemoveMsg(id) {
  const el = document.getElementById(id);
  if (el) el.remove();
}

function aiGetCookie(name) {
  const v = document.cookie.match("(^|;) ?" + name + "=([^;]*)(;|$)");
  return v ? v[2] : null;
}
</script>
"""

# Бүх template файлд нэмэх
template_dirs = [
    "apps/registry/templates/registry",
]

templates = []
for d in template_dirs:
    for f in os.listdir(d):
        if f.endswith(".html"):
            templates.append(os.path.join(d, f))

added = 0
skipped = 0
for path in templates:
    content = open(path, "r", encoding="utf-8").read()
    if "ai-fab" in content:
        # Хуучин widget устгах
        import re
        content = re.sub(r'<!-- AI Зөвлөх Widget -->.*?</script>\s*', '', content, flags=re.DOTALL)
    if "</body>" in content:
        content = content.replace("</body>", chat_widget + "\n</body>", 1)
        open(path, "w", encoding="utf-8").write(content)
        print(f"✅ {f} — нэмэгдлээ")
        added += 1
    else:
        print(f"⚠️ {path} — </body> байхгүй")
        skipped += 1

print(f"\nНийт: {added} файл шинэчлэгдлээ, {skipped} алгасав")