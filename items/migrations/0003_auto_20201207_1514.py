# Generated by Django 3.0.11 on 2020-12-07 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20201203_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemID',
            field=models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='itemID'),
        ),
    ]
