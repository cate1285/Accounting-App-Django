# Generated by Django 3.2.6 on 2021-09-03 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='category',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='quantity',
        ),
        migrations.AddField(
            model_name='staff',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='phone',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Activities', 'Activities'), ('Personal Robin', 'Personal Robin'), ('Food', 'Food'), ('Recibos', 'Recibos'), ('Personal Cate', 'Personal Cate'), ('Arriendo', 'Arriendo'), ('Proyectos', 'Proyectos'), ('Compartidos', 'Compartidos')], max_length=50, null=True),
        ),
    ]
