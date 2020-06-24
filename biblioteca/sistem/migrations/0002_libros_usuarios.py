# Generated by Django 2.2 on 2020-06-24 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('codigo', models.IntegerField(null=True)),
                ('editorial', models.CharField(max_length=50, null=True)),
                ('CantPags', models.IntegerField(null=True)),
                ('CantCopias', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
