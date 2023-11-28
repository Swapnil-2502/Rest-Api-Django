# Generated by Django 4.2.7 on 2023-11-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company_name', models.CharField(blank=True, max_length=150, null=True)),
                ('emp_id', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]