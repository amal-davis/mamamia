# Generated by Django 4.2.5 on 2024-03-16 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mamaapp', '0040_aboutus_aboutus_associates_aboutus_people_why'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faqs',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='faqs',
            name='question',
        ),
        migrations.AddField(
            model_name='faqs',
            name='image',
            field=models.ImageField(default='1', upload_to='mamamia_images/'),
        ),
    ]
