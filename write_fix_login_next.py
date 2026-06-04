content = open("apps/registry/views.py", "r", encoding="utf-8").read()

old = '''def public_login(request):
    if request.user.is_authenticated:
        return redirect("/public/")

    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("/public/")

    return render(request, "registration/login.html", {"form": form})'''

new = '''def public_login(request):
    if request.user.is_authenticated:
        next_url = request.GET.get("next", "/public/")
        return redirect(next_url)

    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.POST.get("next", request.GET.get("next", "/public/"))
            return redirect(next_url)

    next_url = request.GET.get("next", "")
    return render(request, "registration/login.html", {"form": form, "next": next_url})'''

if old in content:
    content = content.replace(old, new, 1)
    open("apps/registry/views.py", "w", encoding="utf-8").write(content)
    print("OK")
else:
    print("NOT FOUND")