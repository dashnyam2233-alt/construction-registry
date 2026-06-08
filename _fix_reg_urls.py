
with open('/var/www/construction-registry/apps/registry/urls.py', 'r') as f:
    s = f.read()

s = s.replace('path("auth/facebook/", auth_facebook, name="auth_facebook"),', '')
s = s.replace('path("auth/emongolia/", auth_emongolia, name="auth_emongolia"),', '')
s = s.replace('path("auth/bank/", auth_bank, name="auth_bank"),', '')

with open('/var/www/construction-registry/apps/registry/urls.py', 'w') as f:
    f.write(s)

print('OK')
