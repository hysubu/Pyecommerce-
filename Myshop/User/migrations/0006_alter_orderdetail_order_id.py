# Generated by Django 4.1 on 2023-08-11 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_addtocart_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='order_id',
            field=models.TextField(blank=True, null=True),
        ),
    ]
