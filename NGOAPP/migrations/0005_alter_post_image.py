# Generated by Django 4.1.6 on 2023-02-12 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGOAPP', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='./post_images'),
        ),
    ]
