# Generated by Django 3.2.12 on 2022-03-20 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_super',
            new_name='is_superuser',
        ),
    ]
