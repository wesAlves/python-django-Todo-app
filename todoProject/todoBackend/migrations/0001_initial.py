# Generated by Django 4.0.3 on 2022-03-21 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
                ('deadline_date', models.DateField()),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]
