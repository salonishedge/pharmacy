# Generated by Django 2.2 on 2019-10-31 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0020_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='numberofproducts',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='total',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
