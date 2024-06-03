# Generated by Django 5.0.6 on 2024-06-02 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.IntegerField()),
                ('receiver_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='blockchain.wallet', to_field='public_address')),
                ('sender_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='blockchain.wallet', to_field='public_address')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
    ]