# Generated by Django 5.1.6 on 2025-02-24 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='denuncias',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Imagen', models.ImageField(blank=True, upload_to='Images/')),
                ('User', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=500)),
                ('date', models.DateField()),
                ('categoria', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
    ]
