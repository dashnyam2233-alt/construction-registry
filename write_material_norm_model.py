import os, sys, django
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

model_code = '''
from django.db import models

class MaterialNorm(models.Model):
    BUILDING_TYPES = [
        ('low_rise', 'Амины орон сууц (1-2 давхар)'),
        ('mid_rise', 'Олон айлын орон сууц (3-9 давхар)'),
        ('high_rise', 'Өндөр давхар (10+ давхар)'),
        ('office', 'Оффисын барилга'),
        ('warehouse', 'Агуулах'),
        ('other', 'Бусад'),
    ]
    WORK_TYPES = [
        ('foundation', 'Суурь'),
        ('wall', 'Хана'),
        ('insulation', 'Дулаалга'),
        ('slab', 'Хучилт'),
        ('roof', 'Дээвэр'),
        ('floor', 'Шал'),
        ('interior', 'Дотор засал'),
        ('window', 'Цонх, хаалга'),
        ('engineering', 'Инженерийн систем'),
        ('labor', 'Ажилчид'),
        ('other', 'Бусад'),
    ]
    building_type = models.CharField('Барилгын төрөл', max_length=20, choices=BUILDING_TYPES)
    work_type = models.CharField('Ажлын төрөл', max_length=20, choices=WORK_TYPES)
    material_name = models.CharField('Материалын нэр', max_length=200)
    norm_per_m2 = models.DecimalField('1м²-д орох норм', max_digits=10, decimal_places=4)
    unit = models.CharField('Нэгж', max_length=20)
    db_category = models.CharField('DB ангилал', max_length=50, blank=True)
    db_name_contains = models.CharField('DB нэр хайх', max_length=100, blank=True)
    notes = models.TextField('Тайлбар', blank=True)
    is_active = models.BooleanField('Идэвхтэй', default=True)

    class Meta:
        verbose_name = 'Материалын норм'
        verbose_name_plural = 'Материалын нормууд'
        ordering = ['building_type', 'work_type']

    def __str__(self):
        return f"{self.get_building_type_display()} | {self.material_name} | {self.norm_per_m2}{self.unit}/м²"
'''

# apps/public/models.py-д нэмэх
models_path = r"apps\public\models.py"
with open(models_path, "r", encoding="utf-8") as f:
    content = f.read()

if 'MaterialNorm' not in content:
    content += model_code
    with open(models_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("OK - MaterialNorm model нэмэгдлээ")
else:
    print("SKIP - аль хэдийн байна")