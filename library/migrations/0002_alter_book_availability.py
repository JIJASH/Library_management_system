# Generated by Django 4.2.6 on 2024-02-09 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='availability',
            field=models.CharField(max_length=10),
        ),
    ]
