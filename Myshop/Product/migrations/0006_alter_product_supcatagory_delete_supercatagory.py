# Generated by Django 4.1 on 2023-07-29 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_remove_product_subcatagory_supercatagory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='supcatagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.subcatagory'),
        ),
        migrations.DeleteModel(
            name='Supercatagory',
        ),
    ]