# Generated by Django 4.2.7 on 2024-02-27 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mamaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SwiperContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slider_images/')),
                ('heading', models.CharField(max_length=255)),
                ('paragraph', models.CharField(max_length=255)),
            ],
        ),
    ]
