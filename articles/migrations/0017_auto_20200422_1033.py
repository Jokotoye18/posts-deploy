# Generated by Django 3.0.3 on 2020-04-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_auto_20200422_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='', max_length=150),
        ),
    ]
