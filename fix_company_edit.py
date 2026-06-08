path = r"D:\Барилгын салбарын бүртгэл\construction_registry_mvp\apps\registry\views.py"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

stub = '''
def company_edit(request, slug):
    from django.shortcuts import get_object_or_404, redirect
    from .models import Company
    company = get_object_or_404(Company, slug=slug)
    return redirect('company_profile', slug=slug)
'''

# Файлын төгсгөлд нэмэх
with open(path, 'a', encoding='utf-8') as f:
    f.write(stub)

print("✅ company_edit нэмэгдлээ")