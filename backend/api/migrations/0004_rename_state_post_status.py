# Generated by Django 4.2 on 2025-02-19 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_category_post_notification_comment_bookmark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='state',
            new_name='status',
        ),
    ]
