# Generated by Django 4.1 on 2023-07-28 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_useraccount_password_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='others',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
