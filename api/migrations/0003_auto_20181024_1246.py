# Generated by Django 2.1 on 2018-10-24 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181024_1122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='name',
            new_name='form',
        ),
    ]
