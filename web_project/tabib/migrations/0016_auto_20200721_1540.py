# Generated by Django 3.0.5 on 2020-07-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabib', '0015_auto_20200721_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='whatssap',
            field=models.IntegerField(default='+2126', max_length=13),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='field',
            field=models.CharField(blank=True, choices=[('a', 'Physiologist'), ('a', 'psychologist'), ('a', 'eyes Doctor'), ('a', 'Dentist')], max_length=30, null=True),
        ),
    ]
