# Generated by Django 4.2.5 on 2024-03-02 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mamaapp', '0033_sperm_guidlines_opening_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sperm_donor_Final',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('paragraph', models.TextField()),
            ],
        ),
    ]
