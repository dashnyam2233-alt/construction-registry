path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\views.py"
with open(path, 'a', encoding='utf-8') as f:
    f.write('''

def api_material_prices(request):
    from django.http import JsonResponse
    return JsonResponse({"status": "ok", "prices": []})

def auth_facebook(request):
    from django.shortcuts import redirect
    return redirect('public_home')

def auth_emongolia(request):
    from django.shortcuts import redirect
    return redirect('public_home')

def auth_bank(request):
    from django.shortcuts import redirect
    return redirect('public_home')
''')
print("✅ Дутуу функцүүд нэмэгдлээ")