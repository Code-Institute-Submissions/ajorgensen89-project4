# Generated by Django 3.2.19 on 2023-06-29 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20230628_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]