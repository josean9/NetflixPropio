# Generated by Django 5.1.3 on 2024-12-05 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0003_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='series',
            field=models.ManyToManyField(related_name='playlists', to='streaming.series'),
        ),
    ]
