# Generated by Django 3.1 on 2020-08-29 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200828_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default='', max_length=20),
        ),
    ]
