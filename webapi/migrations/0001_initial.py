# Generated by Django 3.1.7 on 2021-03-06 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empId', models.IntegerField()),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
            ],
        ),
    ]
