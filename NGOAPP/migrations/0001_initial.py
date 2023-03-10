# Generated by Django 4.1.6 on 2023-02-11 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_name', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=5000)),
                ('is_ngo', models.BooleanField(default=False)),
            ],
        ),
    ]
