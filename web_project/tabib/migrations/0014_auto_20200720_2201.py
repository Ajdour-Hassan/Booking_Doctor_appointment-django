# Generated by Django 3.0.5 on 2020-07-20 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabib', '0013_auto_20200720_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='field',
            field=models.CharField(blank=True, choices=[('a', 'Physiologist'), ('a', 'Dentist'), ('a', 'eyes Doctor'), ('a', 'psychologist')], max_length=30, null=True),
        ),
    ]
