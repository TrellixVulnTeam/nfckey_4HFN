# Generated by Django 2.1.3 on 2018-11-06 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_receivers'),
    ]

    operations = [
        migrations.AddField(
            model_name='receivers',
            name='receiver_dev_id',
            field=models.CharField(default='ff ff ff ff', max_length=16, unique=True),
        ),
    ]