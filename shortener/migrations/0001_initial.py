# Generated by Django 4.1.3 on 2022-11-09 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('alias', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('url', models.URLField(max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_visit', models.DateTimeField(null=True)),
            ],
        ),
    ]