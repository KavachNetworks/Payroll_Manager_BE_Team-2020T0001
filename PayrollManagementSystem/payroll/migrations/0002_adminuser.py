# Generated by Django 3.0.7 on 2020-07-04 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('adminId', models.CharField(max_length=150, primary_key=True, serialize=False, unique=True)),
                ('companyId', models.CharField(max_length=100)),
                ('adminName', models.CharField(max_length=250)),
                ('Password', models.CharField(max_length=250)),
            ],
        ),
    ]
