# Generated by Django 3.2.11 on 2022-01-23 18:48

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='technologies',
            field=modelcluster.fields.ParentalManyToManyField(to='projects.Technology'),
        ),
    ]
