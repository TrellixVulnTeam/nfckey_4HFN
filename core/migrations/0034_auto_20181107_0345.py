# Generated by Django 2.1.3 on 2018-11-06 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_employee_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(default='', null=True),
        ),
    ]