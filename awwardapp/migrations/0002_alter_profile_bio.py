# Generated by Django 4.0.3 on 2022-03-16 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwardapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
