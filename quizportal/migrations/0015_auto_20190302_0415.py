# Generated by Django 2.1.5 on 2019-03-01 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizportal', '0014_auto_20190301_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='section1',
            name='image',
            field=models.ImageField(blank=True, upload_to='pictures'),
        ),
        migrations.AddField(
            model_name='section2',
            name='image',
            field=models.ImageField(blank=True, upload_to='pictures'),
        ),
    ]