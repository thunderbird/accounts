# Generated by Django 5.1.3 on 2024-11-14 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_client_name_alter_clientcontact_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientenvironment',
            name='auth_token',
            field=models.CharField(help_text='The server-to-server/secret auth token', max_length=256, null=True),
        ),
    ]
