# Generated by Django 4.1.6 on 2023-04-05 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_candidate_current_ctc_candidate_current_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='phone_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
