# Generated by Django 2.2 on 2019-10-29 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_auto_20191029_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='total',
        ),
    ]
