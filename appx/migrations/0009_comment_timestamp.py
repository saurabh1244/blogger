# Generated by Django 5.0 on 2024-02-01 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appx', '0008_remove_comment_cum_comment_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
