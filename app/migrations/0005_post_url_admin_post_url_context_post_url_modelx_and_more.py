# Generated by Django 5.0 on 2024-02-17 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_post_admin_post_html_page1_post_html_page2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url_admin',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='url_context',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='url_modelx',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='url_setting',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='url_view',
            field=models.TextField(blank=True),
        ),
    ]
