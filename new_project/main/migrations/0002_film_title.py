# Generated by Django 4.1.2 on 2022-11-03 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='title',
            field=models.CharField(default='no name', max_length=100),
        ),
    ]
