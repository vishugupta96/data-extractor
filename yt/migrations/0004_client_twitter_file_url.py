# Generated by Django 3.2.10 on 2022-02-10 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yt', '0003_client_twetter_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='twitter_file_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
