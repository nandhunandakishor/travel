# Generated by Django 5.1 on 2024-10-23 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelblogapp', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='bachelor_package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Phonenumber', models.IntegerField(max_length=10)),
                ('Checkin', models.DateField(max_length=100)),
                ('Checkout', models.DateField(max_length=100)),
                ('Roomtype', models.CharField(max_length=100)),
                ('Numberofguest', models.IntegerField(max_length=100)),
                ('Specialrequest', models.CharField(max_length=200)),
            ],
        ),
    ]
