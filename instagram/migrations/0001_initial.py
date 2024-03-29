# Generated by Django 3.0.14 on 2022-05-19 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='instagram/post/%y년/%m월/%d일')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
