# Generated by Django 2.1.7 on 2019-03-03 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customer_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='created',
        ),
    ]
