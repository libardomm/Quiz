# Generated by Django 2.0.2 on 2018-02-20 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='questions',
            field=models.ManyToManyField(to='quiz.Question'),
        ),
    ]
