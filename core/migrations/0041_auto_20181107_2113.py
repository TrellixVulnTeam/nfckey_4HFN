# Generated by Django 2.1.3 on 2018-11-07 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20181107_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='publications',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
    ]