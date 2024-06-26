# Generated by Django 5.0.6 on 2024-06-04 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0002_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.FloatField(default=0.0),
        ),
    ]
