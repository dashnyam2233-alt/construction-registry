# apps/registry/urls.py-аас otp import-г comment болгох
import re

path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\urls.py"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# otp import-г comment болгох
content = content.replace(
    'from .otp_views import send_otp, verify_otp',
    '# from .otp_views import send_otp, verify_otp'
)

# otp url-уудыг comment болгох
content = re.sub(r"^\s*path\(['\"].*otp.*['\"].*\),?\s*$", 
                 lambda m: '    # ' + m.group().strip(), 
                 content, flags=re.MULTILINE | re.IGNORECASE)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ otp_views comment болгогдлоо")