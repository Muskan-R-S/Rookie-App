# Generated by Django 4.1.6 on 2023-04-05 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_mandates'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mandates',
            new_name='Mandate',
        ),
    ]
