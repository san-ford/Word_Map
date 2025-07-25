# Generated by Django 5.2.2 on 2025-06-07 22:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_text', models.CharField(max_length=200)),
                ('req_date', models.DateTimeField(verbose_name='date requested')),
            ],
        ),
        migrations.CreateModel(
            name='WordOutput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_text', models.CharField(max_length=200)),
                ('input', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='word_retrieval.wordinput')),
            ],
        ),
    ]
