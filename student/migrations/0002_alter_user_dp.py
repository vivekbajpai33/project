# Generated by Django 4.2.3 on 2023-07-14 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dp',
            field=models.FileField(upload_to='student'),
        ),
    ]