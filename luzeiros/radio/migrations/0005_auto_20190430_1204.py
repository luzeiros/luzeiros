# Generated by Django 2.2 on 2019-04-30 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0004_auto_20190430_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(blank=True),
        ),
    ]
