# Generated by Django 2.1.5 on 2019-03-01 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizportal', '0012_auto_20190228_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='section3',
            name='image',
            field=models.FileField(blank=True, upload_to='pictures'),
        ),
    ]