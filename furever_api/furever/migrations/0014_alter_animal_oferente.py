# Generated by Django 4.2.5 on 2023-10-17 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('furever', '0013_conexion_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='oferente',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='furever.oferente'),
        ),
    ]
