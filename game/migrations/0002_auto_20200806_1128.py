# Generated by Django 3.0.7 on 2020-08-06 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstreaks',
            name='last_played',
            field=models.DateField(null=True),
        ),
    ]