# Generated by Django 4.2 on 2023-05-14 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_order_total_bonuses_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email for invoice sending'),
        ),
    ]