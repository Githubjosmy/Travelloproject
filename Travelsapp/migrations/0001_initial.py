# Generated by Django 4.1.3 on 2022-12-07 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='Pics')),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
