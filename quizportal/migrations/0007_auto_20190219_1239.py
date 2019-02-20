# Generated by Django 2.1.5 on 2019-02-19 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizportal', '0006_auto_20190219_0235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solvedq1',
            name='q_idsol',
        ),
        migrations.RemoveField(
            model_name='solvedq1',
            name='q_idunsol',
        ),
        migrations.RemoveField(
            model_name='solvedq2',
            name='q_idsol',
        ),
        migrations.RemoveField(
            model_name='solvedq2',
            name='q_idunsol',
        ),
        migrations.RemoveField(
            model_name='solvedq3',
            name='q_idsol',
        ),
        migrations.RemoveField(
            model_name='solvedq3',
            name='q_idunsol',
        ),
        migrations.AddField(
            model_name='solvedq1',
            name='check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='solvedq1',
            name='q_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quizportal.Section1'),
        ),
        migrations.AddField(
            model_name='solvedq2',
            name='check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='solvedq2',
            name='q_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quizportal.Section2'),
        ),
        migrations.AddField(
            model_name='solvedq3',
            name='check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='solvedq3',
            name='q_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quizportal.Section3'),
        ),
    ]