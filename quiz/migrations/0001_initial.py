# Generated by Django 2.0.2 on 2018-02-19 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(help_text='Ingrese  la pregunta que quiere mostrar', max_length=1000)),
            ],
        ),
    ]
