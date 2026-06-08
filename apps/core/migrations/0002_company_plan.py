from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]
    operations = [
        migrations.AddField(
            model_name="company",
            name="plan",
            field=models.CharField(
                verbose_name="Багцын төрөл",
                max_length=20,
                choices=[
                    ("free", "Үнэгүй"),
                    ("standard", "Стандарт"),
                    ("premium", "Премиум"),
                ],
                default="free",
            ),
        ),
        migrations.AddField(
            model_name="company",
            name="plan_expires",
            field=models.DateField(
                verbose_name="Багц дуусах огноо",
                null=True,
                blank=True,
            ),
        ),
    ]
