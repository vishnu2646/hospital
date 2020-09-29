# Generated by Django 3.0.4 on 2020-06-25 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0003_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appoinment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('reason', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField()),
                ('phone', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
