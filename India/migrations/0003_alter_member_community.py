# Generated by Django 4.1.5 on 2023-05-22 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('India', '0002_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='community',
            field=models.ManyToManyField(related_name='community', to='India.map'),
        ),
    ]
