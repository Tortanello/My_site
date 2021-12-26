# Generated by Django 3.1 on 2020-08-21 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('post', models.TextField()),
                ('img', models.ImageField(upload_to='')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('comment', models.CharField(max_length=500)),
                ('date', models.DateTimeField()),
                ('idPost', models.IntegerField()),
            ],
        ),
    ]
