# Generated by Django 2.2.24 on 2021-07-12 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookpage', '0004_auto_20210710_2110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manga',
            old_name='publisher_date',
            new_name='publish_date',
        ),
    ]
