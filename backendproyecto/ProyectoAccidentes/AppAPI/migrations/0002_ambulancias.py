# Generated by Django 3.2.4 on 2022-11-28 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulancias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Identificacion', models.CharField(max_length=20)),
                ('TipoHerida', models.CharField(max_length=20)),
                ('CantidadH', models.FloatField()),
            ],
        ),
    ]
    

