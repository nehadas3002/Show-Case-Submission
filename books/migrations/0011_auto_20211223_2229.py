# Generated by Django 3.2.7 on 2021-12-24 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_newbook_synopsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='newbook',
            name='synopsis',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
    ]
