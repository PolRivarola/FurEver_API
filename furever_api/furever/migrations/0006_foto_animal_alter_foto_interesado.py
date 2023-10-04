# Generated by Django 4.2.5 on 2023-10-04 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('furever', '0005_alter_animal_oferente'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='animal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='furever.animal'),
        ),
        migrations.AlterField(
            model_name='foto',
            name='interesado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='furever.interesado'),
        ),
    ]
