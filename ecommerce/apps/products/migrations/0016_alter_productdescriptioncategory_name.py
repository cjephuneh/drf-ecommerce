# Generated by Django 4.2 on 2023-05-17 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_productcharacteristics_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdescriptioncategory',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Description category name'),
        ),
    ]