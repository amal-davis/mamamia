# Generated by Django 4.2.7 on 2024-02-29 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mamaapp', '0012_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='mamamia_images/')),
            ],
        ),
    ]
