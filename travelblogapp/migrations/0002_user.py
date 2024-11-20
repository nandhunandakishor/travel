# Generated by Django 5.1 on 2024-09-30 07:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelblogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=50)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelblogapp.blog')),
            ],
        ),
    ]