# Generated by Django 3.0.11 on 2020-12-06 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20201203_0457'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='items',
            field=models.ManyToManyField(blank=True, to='items.Item'),
        ),
    ]
