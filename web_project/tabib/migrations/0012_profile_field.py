# Generated by Django 3.0.5 on 2020-07-20 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabib', '0011_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='field',
            field=models.CharField(blank=True, choices=[('a', 'psychologist'), ('a', 'eyes Doctor'), ('a', 'Dentist'), ('a', 'Physiologist')], max_length=30, null=True),
        ),
    ]
