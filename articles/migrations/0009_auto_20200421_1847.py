# Generated by Django 3.0.3 on 2020-04-21 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20200421_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
