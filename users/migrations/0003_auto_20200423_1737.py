# Generated by Django 3.0.5 on 2020-04-23 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='id',
        ),
        migrations.AlterField(
            model_name='code',
            name='code',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
    ]
