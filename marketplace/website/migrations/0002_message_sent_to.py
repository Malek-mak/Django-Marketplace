# Generated by Django 5.1.5 on 2025-06-15 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sent_to',
            field=models.TextField(null=True),
        ),
    ]
