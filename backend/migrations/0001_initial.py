# Generated by Django 4.0 on 2024-08-27 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('Ford', 'Ford'), ('Chevrolet', 'Chevrolet'), ('Toyota', 'Toyota'), ('Honda', 'Honda'), ('Volkswagen', 'Volkswagen'), ('Fiat', 'Fiat'), ('Hyundai', 'Hyundai')], max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('license_plate', models.CharField(max_length=10)),
                ('year', models.PositiveIntegerField()),
                ('owner_name', models.CharField(max_length=100)),
                ('owner_phone', models.CharField(max_length=20)),
                ('problem_description', models.TextField()),
                ('service_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
