# Generated by Django 3.0.7 on 2020-08-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200719_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='views',
        ),
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
