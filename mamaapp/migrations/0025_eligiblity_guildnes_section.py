# Generated by Django 4.2.5 on 2024-03-02 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mamaapp', '0024_guidlines'),
    ]

    operations = [
        migrations.CreateModel(
            name='eligiblity_guildnes_Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('paragraph', models.TextField()),
                ('other_content', models.TextField()),
            ],
        ),
    ]
