# Generated by Django 4.0.6 on 2022-07-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
    ]
