# Generated by Django 4.1 on 2022-08-19 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_manager', '0002_alter_post_telephone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='key_help_words',
        ),
    ]