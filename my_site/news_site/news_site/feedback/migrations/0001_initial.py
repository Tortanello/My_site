# Generated by Django 3.1 on 2020-08-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('proposal', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
