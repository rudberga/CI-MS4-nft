# Generated by Django 3.2 on 2021-04-15 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0004_auto_20210415_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='year',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True),
        ),
    ]
