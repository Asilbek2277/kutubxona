# Generated by Django 5.0.1 on 2024-01-28 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy', '0006_alter_kutubxonachi_ish_vaqti_alter_kutubxonachi_ism'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='qaytarish_sana',
            field=models.DateField(blank=True, null=True),
        ),
    ]
