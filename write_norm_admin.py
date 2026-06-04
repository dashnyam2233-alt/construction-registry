path = r"apps\public\admin.py"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

admin_code = '''
@admin.register(MaterialNorm)
class MaterialNormAdmin(admin.ModelAdmin):
    list_display = ['building_type', 'work_type', 'material_name', 'norm_per_m2', 'unit', 'db_category', 'is_active']
    list_filter = ['building_type', 'work_type', 'is_active']
    search_fields = ['material_name', 'db_category', 'db_name_contains']
    list_editable = ['norm_per_m2', 'is_active']
    ordering = ['building_type', 'work_type', 'material_name']
    list_per_page = 50
'''

if 'MaterialNorm' not in content:
    # Import нэмэх
    old = 'from .models import'
    if old in content:
        first_import = content.find(old)
        end_of_line = content.find('\n', first_import)
        content = content[:end_of_line] + ', MaterialNorm' + content[end_of_line:]
    content += admin_code
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("OK - MaterialNorm admin нэмэгдлээ")
else:
    print("SKIP - аль хэдийн байна")