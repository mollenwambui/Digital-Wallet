# Generated by Django 4.0.6 on 2022-08-19 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_alter_customer_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
