import os

templates = {
    "templates/registration/password_reset_form.html": """<!doctype html>
<html lang="mn">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Нууц үг сэргээх</title>
  <style>
    *{box-sizing:border-box;margin:0;padding:0;}
    body{font-family:system-ui,sans-serif;background:#f0f4f8;min-height:100vh;display:grid;place-items:center;padding:24px;}
    .card{width:min(400px,94vw);background:#fff;border:1px solid #e2e8f0;border-radius:16px;padding:32px;}
    .logo{text-align:center;margin-bottom:24px;}
    .logo-icon{width:48px;height:48px;background:#2f6477;border-radius:10px;display:inline-flex;align-items:center;justify-content:center;margin-bottom:10px;}
    .logo-icon svg{width:26px;height:26px;fill:none;stroke:#fff;stroke-width:2;}
    h1{font-size:16px;font-weight:600;color:#1a202c;margin-bottom:4px;}
    p{font-size:13px;color:#718096;margin-bottom:16px;}
    label{display:block;font-size:12px;font-weight:600;color:#4a5568;margin-bottom:5px;}
    input{width:100%;padding:9px 12px;border:1px solid #e2e8f0;border-radius:8px;font-size:14px;color:#1a202c;outline:none;margin-bottom:14px;}
    input:focus{border-color:#2f6477;}
    .btn{width:100%;padding:10px;background:#2f6477;color:#fff;border:none;border-radius:8px;font-size:14px;font-weight:600;cursor:pointer;}
    .footer{text-align:center;margin-top:14px;font-size:12px;}
    .footer a{color:#2f6477;text-decoration:none;}
  </style>
</head>
<body>
  <div class="card">
    <div class="logo">
      <div class="logo-icon">
        <svg viewBox="0 0 24 24"><path d="M3 21h18M3 7l9-4 9 4M4 7v14M20 7v14M9 21v-6h6v6"/></svg>
      </div>
      <h1>Нууц үг сэргээх</h1>
      <p>И-мэйл хаягаа оруулна уу. Нууц үг сэргээх холбоос илгээнэ.</p>
    </div>
    <form method="post">
      {% csrf_token %}
      <label for="id_email">И-мэйл хаяг</label>
      <input type="email" name="email" id="id_email" placeholder="email@example.mn" autofocus>
      <button type="submit" class="btn">Холбоос илгээх</button>
    </form>
    <div class="footer"><a href="/login/">Нэвтрэх рүү буцах</a></div>
  </div>
</body>
</html>""",

    "templates/registration/password_reset_done.html": """<!doctype html>
<html lang="mn">
<head>
  <meta charset="utf-8">
  <title>И-мэйл илгээгдлээ</title>
  <style>
    *{box-sizing:border-box;margin:0;padding:0;}
    body{font-family:system-ui,sans-serif;background:#f0f4f8;min-height:100vh;display:grid;place-items:center;padding:24px;}
    .card{width:min(400px,94vw);background:#fff;border:1px solid #e2e8f0;border-radius:16px;padding:32px;text-align:center;}
    .icon{font-size:48px;margin-bottom:16px;}
    h1{font-size:16px;font-weight:600;color:#1a202c;margin-bottom:8px;}
    p{font-size:13px;color:#718096;margin-bottom:16px;}
    a{color:#2f6477;text-decoration:none;font-size:13px;}
  </style>
</head>
<body>
  <div class="card">
    <div class="icon">📧</div>
    <h1>И-мэйл илгээгдлээ</h1>
    <p>Нууц үг сэргээх холбоосыг таны и-мэйл рүү илгээлээ. И-мэйлээ шалгаарай.</p>
    <a href="/login/">Нэвтрэх рүү буцах</a>
  </div>
</body>
</html>""",

    "templates/registration/password_reset_confirm.html": """<!doctype html>
<html lang="mn">
<head>
  <meta charset="utf-8">
  <title>Шинэ нууц үг</title>
  <style>
    *{box-sizing:border-box;margin:0;padding:0;}
    body{font-family:system-ui,sans-serif;background:#f0f4f8;min-height:100vh;display:grid;place-items:center;padding:24px;}
    .card{width:min(400px,94vw);background:#fff;border:1px solid #e2e8f0;border-radius:16px;padding:32px;}
    .logo{text-align:center;margin-bottom:20px;}
    h1{font-size:16px;font-weight:600;color:#1a202c;margin-bottom:4px;text-align:center;}
    p{font-size:13px;color:#718096;margin-bottom:16px;text-align:center;}
    label{display:block;font-size:12px;font-weight:600;color:#4a5568;margin-bottom:5px;}
    input{width:100%;padding:9px 12px;border:1px solid #e2e8f0;border-radius:8px;font-size:14px;color:#1a202c;outline:none;margin-bottom:14px;}
    input:focus{border-color:#2f6477;}
    .btn{width:100%;padding:10px;background:#2f6477;color:#fff;border:none;border-radius:8px;font-size:14px;font-weight:600;cursor:pointer;}
  </style>
</head>
<body>
  <div class="card">
    <h1>Шинэ нууц үг тавих</h1>
    <p>Шинэ нууц үгээ оруулна уу</p>
    {% if validlink %}
    <form method="post">
      {% csrf_token %}
      <label>Шинэ нууц үг</label>
      <input type="password" name="new_password1" placeholder="••••••••">
      <label>Давтах</label>
      <input type="password" name="new_password2" placeholder="••••••••">
      <button type="submit" class="btn">Нууц үг солих</button>
    </form>
    {% else %}
    <p style="color:#c53030;">Холбоос хүчингүй болсон байна. Дахин нууц үг сэргээх хүсэлт илгээнэ үү.</p>
    <a href="/accounts/password-reset/" style="color:#2f6477;">Дахин оролдох</a>
    {% endif %}
  </div>
</body>
</html>""",

    "templates/registration/password_reset_complete.html": """<!doctype html>
<html lang="mn">
<head>
  <meta charset="utf-8">
  <title>Нууц үг солигдлоо</title>
  <style>
    *{box-sizing:border-box;margin:0;padding:0;}
    body{font-family:system-ui,sans-serif;background:#f0f4f8;min-height:100vh;display:grid;place-items:center;padding:24px;}
    .card{width:min(400px,94vw);background:#fff;border:1px solid #e2e8f0;border-radius:16px;padding:32px;text-align:center;}
    .icon{font-size:48px;margin-bottom:16px;}
    h1{font-size:16px;font-weight:600;color:#1a202c;margin-bottom:8px;}
    p{font-size:13px;color:#718096;margin-bottom:16px;}
    a{display:inline-block;padding:10px 24px;background:#2f6477;color:#fff;border-radius:8px;text-decoration:none;font-size:14px;font-weight:600;}
  </style>
</head>
<body>
  <div class="card">
    <div class="icon">✅</div>
    <h1>Нууц үг амжилттай солигдлоо</h1>
    <p>Шинэ нууц үгээрээ нэвтэрч болно.</p>
    <a href="/login/">Нэвтрэх</a>
  </div>
</body>
</html>"""
}

for path, content in templates.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"OK: {path}")