# Generated by Django 4.2.5 on 2023-09-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, unique=True)),
                ('phone_number_user', models.CharField(max_length=100, unique=True)),
                ('contry_user', models.CharField(max_length=100, unique=True)),
                ('gender_user', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]