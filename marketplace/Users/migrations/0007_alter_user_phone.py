# Generated by Django 5.1.5 on 2025-07-21 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, default='000-000-0000', max_length=15, null=True),
        ),
    ]
