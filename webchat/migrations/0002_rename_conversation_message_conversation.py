# Generated by Django 4.2.10 on 2024-02-18 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webchat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='Conversation',
            new_name='conversation',
        ),
    ]
