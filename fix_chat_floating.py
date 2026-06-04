content = open("apps/registry/templates/registry/budget_calculator.html", "r", encoding="utf-8").read()

# Chat section-г устгах
import re
old_section = re.search(r'<div class="chat-section">.*?</div>\s*\n\s*<div class="page">', content, re.DOTALL)
if old_section:
    content = content[:old_section.start()] + '<div class="page">' + content[old_section.end():]
    print("OK — chat section устгагдлаа")
else:
    print("NOT FOUND — chat section")

# CSS-д floating chat нэмэх
old_css = '.chat-section{'
new_css = '''.float-btn{position:fixed;bottom:24px;right:24px;width:56px;height:56px;background:#f59e0b;border:none;border-radius:50%;font-size:24px;cursor:pointer;box-shadow:0 4px 16px rgba(0,0,0,0.2);z-index:2000;display:flex;align-items:center;justify-content:center;transition:transform 0.2s;}
    .float-btn:hover{transform:scale(1.1);}
    .float-chat{position:fixed;bottom:90px;right:24px;width:360px;background:#fff;border:0.5px solid #e2e8f0;border-radius:16px;box-shadow:0 8px 32px rgba(0,0,0,0.15);z-index:2000;display:none;flex-direction:column;overflow:hidden;}
    .float-chat.open{display:flex;}
    .float-chat-hd{background:#1e3a4a;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;}
    .float-chat-hd-t{color:#fff;font-size:14px;font-weight:700;}
    .float-chat-hd-s{color:#94a3b8;font-size:11px;margin-top:2px;}
    .float-chat-close{color:#94a3b8;background:none;border:none;font-size:18px;cursor:pointer;padding:0;}
    .float-chat-close:hover{color:#fff;}
    .chat-messages{background:#f8fafc;padding:14px;min-height:200px;max-height:340px;overflow-y:auto;display:flex;flex-direction:column;gap:10px;}
    .msg{display:flex;gap:8px;align-items:flex-start;}
    .msg.user{flex-direction:row-reverse;}
    .msg-avatar{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0;background:#f1f5f9;}
    .msg.user .msg-avatar{background:#fef3c7;}
    .msg-bubble{border-radius:12px;padding:8px 12px;font-size:12px;line-height:1.6;color:#1e293b;max-width:85%;}
    .msg.ai .msg-bubble{background:#fff;border:0.5px solid #e2e8f0;}
    .msg.user .msg-bubble{background:#fef3c7;border:0.5px solid #f59e0b;}
    .typing .msg-bubble{color:#94a3b8;font-style:italic;}
    .float-chat-input{padding:10px;border-top:0.5px solid #e2e8f0;display:flex;gap:6px;background:#fff;}
    .chat-input{flex:1;padding:8px 12px;border:1px solid #e2e8f0;border-radius:8px;font-size:12px;outline:none;}
    .chat-input:focus{border-color:#f59e0b;}
    .chat-send{padding:8px 14px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:8px;font-size:14px;cursor:pointer;font-weight:700;}
    .chat-send:hover{background:#e08c00;}
    .chat-section{display:none;}
    .chat-section{'''

if old_css in content:
    content = content.replace(old_css, new_css, 1)
    print("OK — CSS шинэчлэгдлээ")
else:
    # CSS байхгүй бол шинээр нэмэх
    content = content.replace('</style>', '''.float-btn{position:fixed;bottom:24px;right:24px;width:56px;height:56px;background:#f59e0b;border:none;border-radius:50%;font-size:24px;cursor:pointer;box-shadow:0 4px 16px rgba(0,0,0,0.2);z-index:2000;display:flex;align-items:center;justify-content:center;transition:transform 0.2s;}
    .float-btn:hover{transform:scale(1.1);}
    .float-chat{position:fixed;bottom:90px;right:24px;width:360px;background:#fff;border:0.5px solid #e2e8f0;border-radius:16px;box-shadow:0 8px 32px rgba(0,0,0,0.15);z-index:2000;display:none;flex-direction:column;overflow:hidden;}
    .float-chat.open{display:flex;}
    .float-chat-hd{background:#1e3a4a;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;}
    .float-chat-hd-t{color:#fff;font-size:14px;font-weight:700;}
    .float-chat-hd-s{color:#94a3b8;font-size:11px;margin-top:2px;}
    .float-chat-close{color:#94a3b8;background:none;border:none;font-size:18px;cursor:pointer;padding:0;}
    .float-chat-close:hover{color:#fff;}
    .chat-messages{background:#f8fafc;padding:14px;min-height:200px;max-height:340px;overflow-y:auto;display:flex;flex-direction:column;gap:10px;}
    .msg{display:flex;gap:8px;align-items:flex-start;}
    .msg.user{flex-direction:row-reverse;}
    .msg-avatar{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0;background:#f1f5f9;}
    .msg.user .msg-avatar{background:#fef3c7;}
    .msg-bubble{border-radius:12px;padding:8px 12px;font-size:12px;line-height:1.6;color:#1e293b;max-width:85%;}
    .msg.ai .msg-bubble{background:#fff;border:0.5px solid #e2e8f0;}
    .msg.user .msg-bubble{background:#fef3c7;border:0.5px solid #f59e0b;}
    .typing .msg-bubble{color:#94a3b8;font-style:italic;}
    .float-chat-input{padding:10px;border-top:0.5px solid #e2e8f0;display:flex;gap:6px;background:#fff;}
    .chat-input{flex:1;padding:8px 12px;border:1px solid #e2e8f0;border-radius:8px;font-size:12px;outline:none;}
    .chat-input:focus{border-color:#f59e0b;}
    .chat-send{padding:8px 14px;background:#f59e0b;color:#1e3a4a;border:none;border-radius:8px;font-size:14px;cursor:pointer;font-weight:700;}
    .chat-send:hover{background:#e08c00;}
    </style>''', 1)
    print("OK — CSS шинээр нэмэгдлээ")

# Floating chat HTML нэмэх
old_body = '</body>'
new_body = '''<!-- Floating Chat -->
<button class="float-btn" onclick="toggleChat()" id="float-btn" title="AI Зөвлөгөө">🤖</button>

<div class="float-chat" id="float-chat">
  <div class="float-chat-hd">
    <div>
      <div class="float-chat-hd-t">🤖 Барилгын AI Зөвлөгөө</div>
      <div class="float-chat-hd-s">Барилгатай холбоотой асуул</div>
    </div>
    <button class="float-chat-close" onclick="toggleChat()">✕</button>
  </div>
  <div class="chat-messages" id="chat-messages">
    <div class="msg ai">
      <div class="msg-avatar">🤖</div>
      <div class="msg-bubble">Сайн байна уу! Барилгатай холбоотой асуулт байвал асуугаарай.<br><br>• Зөвшөөрөл яаж авах вэ?<br>• Барилгын компани яаж сонгох вэ?<br>• Ямар материал сайн вэ?</div>
    </div>
  </div>
  <div class="float-chat-input">
    <input type="text" id="chat-input" class="chat-input" placeholder="Асуултаа бичнэ үү..." onkeydown="if(event.key==='Enter') sendChat()">
    <button class="chat-send" onclick="sendChat()">➤</button>
  </div>
</div>

</body>'''

content = content.replace(old_body, new_body, 1)
print("OK — floating chat HTML нэмэгдлээ")

# toggleChat JS нэмэх
old_js = 'const chatHistory = [];'
new_js = '''const chatHistory = [];

function toggleChat() {
  const chat = document.getElementById("float-chat");
  const btn = document.getElementById("float-btn");
  chat.classList.toggle("open");
  btn.textContent = chat.classList.contains("open") ? "✕" : "🤖";
  if (chat.classList.contains("open")) {
    document.getElementById("chat-input").focus();
  }
}

'''
content = content.replace(old_js, new_js, 1)
print("OK — toggleChat JS нэмэгдлээ")

open("apps/registry/templates/registry/budget_calculator.html", "w", encoding="utf-8").write(content)
print("Хадгалагдлаа")