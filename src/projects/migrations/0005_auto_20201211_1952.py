# Generated by Django 3.1.2 on 2020-12-12 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20201108_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
