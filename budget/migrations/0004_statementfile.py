# Generated by Django 5.1.1 on 2024-10-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatementFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
