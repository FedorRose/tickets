# Generated by Django 4.0.6 on 2022-08-10 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_ticket_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='time',
            field=models.PositiveIntegerField(default=0),
        ),
    ]