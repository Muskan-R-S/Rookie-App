# Generated by Django 4.0 on 2021-12-28 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='current_ctc',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='current_role',
            field=models.CharField(default='Null', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='email_id',
            field=models.CharField(default='Null', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='experience',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='phone_no',
            field=models.CharField(default='Null', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='status',
            field=models.CharField(choices=[('cv_surfaced', 'CV Surfaced'), ('round_1', 'Round 1'), ('round_2', 'Round 2'), ('round_3', 'Round 3'), ('offered', 'Offered'), ('candidate_backed', 'Candidate Backed'), ('offer_dropped', 'Offer Dropped'), ('hr_reject', 'HR reject'), ('reject', 'Reject'), ('not_a_fit', 'Not a fit'), ('offer_negotiation', 'Offer Negotiation')], default='CV surfaced', max_length=30),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
