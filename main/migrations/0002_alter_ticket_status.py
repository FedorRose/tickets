# Generated by Django 4.0.6 on 2022-08-06 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('NEW', 'NEW'), ('ASSIGNED-DEV', 'ASSIGNED-DEV'), ('REVIEW-NEEDED', 'REVIEW-NEEDED'), ('RESOLVED-DEV', 'RESOLVED-DEV'), ('CLOSED', 'CLOSED')], default='NEW', max_length=30),
        ),
    ]