# Generated by Django 2.1.7 on 2019-03-02 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('number_employees', models.CharField(max_length=10)),
            ],
        ),
    ]