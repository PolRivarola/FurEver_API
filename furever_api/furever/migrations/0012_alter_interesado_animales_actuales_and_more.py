# Generated by Django 4.2.5 on 2023-10-14 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furever', '0011_alter_documentacion_doc_alter_foto_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interesado',
            name='animales_actuales',
            field=models.BooleanField(blank=True, null=True, verbose_name='Animales Actuales'),
        ),
        migrations.AlterField(
            model_name='interesado',
            name='animales_previos',
            field=models.BooleanField(blank=True, null=True, verbose_name='Animales Previos'),
        ),
        migrations.AlterField(
            model_name='interesado',
            name='ninos',
            field=models.BooleanField(blank=True, null=True, verbose_name='Niños'),
        ),
    ]
