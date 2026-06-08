
with open('/var/www/construction-registry/apps/registry/views.py', 'r') as f:
    s = f.read()

old = '''def auth_facebook(request):
    return render(request, "registry/auth_stub.html", {"provider": "Facebook"})
def auth_emongolia(request):
    return render(request, "registry/auth_stub.html", {"provider": "e-Mongolia"})
def auth_bank(request):
    return render(request, "registry/auth_stub.html", {"provider": "Bankny kod"})'''

new = '''def auth_facebook(request):
    from django.shortcuts import redirect
    return redirect('/auth/social/login/facebook/')
def auth_emongolia(request):
    return render(request, "registry/auth_stub.html", {"provider": "e-Mongolia"})
def auth_bank(request):
    return render(request, "registry/auth_stub.html", {"provider": "Bankny kod"})'''

s = s.replace(old, new)

with open('/var/www/construction-registry/apps/registry/views.py', 'w') as f:
    f.write(s)

print('OK')
