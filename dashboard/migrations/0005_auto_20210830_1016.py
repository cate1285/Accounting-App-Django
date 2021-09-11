# Generated by Django 3.2.6 on 2021-08-30 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210320_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='category',
            field=models.CharField(choices=[('Activities', 'Activities'), ('Cleaning', 'Cleaning'), ('Food', 'Food')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Activities', 'Activities'), ('Cleaning', 'Cleaning'), ('Food', 'Food')], max_length=50, null=True),
        ),
    ]
