# Generated by Django 3.1.2 on 2020-12-12 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_delete_ticket'),
        ('tickets', '0003_auto_20201212_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='personnel',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_ticket', to='projects.projectmember'),
        ),
    ]