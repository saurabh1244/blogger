# Generated by Django 5.0 on 2024-02-18 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='post',
            new_name='cum_id',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='cmt',
            new_name='text',
        ),
    ]
