# Generated by Django 4.1.6 on 2023-10-02 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furever', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='especie',
            field=models.CharField(choices=[('P', 'Perro'), ('G', 'Gato'), ('C', 'Conejo'), ('T', 'Tortuga'), ('S', 'Serpiente'), ('O', 'Otros')], default='P', max_length=20),
        ),
        migrations.AlterField(
            model_name='animalventa',
            name='cantidad',
            field=models.IntegerField(default=False, verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='animalventa',
            name='garrapata',
            field=models.BooleanField(default=False, verbose_name='Garrapata'),
        ),
        migrations.AlterField(
            model_name='animalventa',
            name='marca_liquida',
            field=models.BooleanField(default=False, verbose_name='Marca líquida'),
        ),
        migrations.AlterField(
            model_name='animalventa',
            name='mio_mio',
            field=models.BooleanField(default=False, verbose_name='Mio Mio'),
        ),
        migrations.AlterField(
            model_name='animalventa',
            name='precio',
            field=models.FloatField(default=False, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='animalventa',
            name='sanidad',
            field=models.BooleanField(default=False, verbose_name='Sanidad'),
        ),
        migrations.AlterField(
            model_name='animalventa',
            name='trazada',
            field=models.BooleanField(default=False, verbose_name='Trazada'),
        ),
        migrations.AlterField(
            model_name='animalventa',
            name='uniformidad',
            field=models.BooleanField(default=False, verbose_name='Uniformidad'),
        ),
    ]