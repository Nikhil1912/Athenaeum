# Generated by Django 4.1.1 on 2022-09-14 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athenaeum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='books',
            name='isInStock',
            field=models.BooleanField(default=False),
        ),
    ]
