# Generated by Django 2.1.5 on 2024-11-11 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy_analysis', '0004_auto_20241111_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackedsite',
            name='latest_policy',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]