# Generated by Django 4.2 on 2025-02-18 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='fullname',
            new_name='full_name',
        ),
    ]
