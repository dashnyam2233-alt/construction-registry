import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.registry.views import calculate_engineering_budget

test_data = {
    'eng_type': 'heat_pit',
    'length': '3.5',
    'width': '1.5', 
    'depth': '2.3',
    'wall_thick': '0.45',
    'concrete_grade': 'B25',
    'quality': 'дунд',
    'location': 'Улаанбаатар',
}

result = calculate_engineering_budget(test_data)
print("RESULT:", result)