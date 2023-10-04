# Generated by Django 4.2.5 on 2023-10-04 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('furever', '0003_alter_animal_peso'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='oferente',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='furever.interesado'),
        ),
        migrations.AlterField(
            model_name='conexion',
            name='animal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='furever.animaladopcion'),
        ),
        migrations.AlterField(
            model_name='conexion',
            name='interesado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='furever.interesado'),
        ),
        migrations.AlterField(
            model_name='conexion',
            name='oferente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='furever.oferente'),
        ),
        migrations.AlterField(
            model_name='documentacion',
            name='oferente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='furever.oferente'),
        ),
        migrations.AlterField(
            model_name='foto',
            name='interesado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='furever.interesado'),
        ),
    ]
