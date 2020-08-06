# Generated by Django 3.0.7 on 2020-08-06 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_question_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[('easy', 'Easy'), ('difficult', 'Difficult'), ('medium', 'Medium')], default='easy', max_length=20),
        ),
    ]
