# Generated by Django 2.2.9 on 2020-06-11 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190827_1505'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'default_permissions': ('add',), 'permissions': (('read', 'Can read'),)},
        ),
    ]
