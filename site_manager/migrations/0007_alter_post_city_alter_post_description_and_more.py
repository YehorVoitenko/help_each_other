# Generated by Django 4.1 on 2022-08-20 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_manager', '0006_alter_post_name_alter_post_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='city',
            field=models.TextField(max_length=50, null=True, verbose_name='Enter city, you live'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(null=True, verbose_name='Enter description'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.TextField(max_length=50, null=True, verbose_name='Enter your name'),
        ),
        migrations.AlterField(
            model_name='post',
            name='surname',
            field=models.TextField(max_length=50, null=True, verbose_name='Enter your surname'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(max_length=50, null=True, verbose_name='Enter title'),
        ),
    ]
