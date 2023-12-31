# Generated by Django 4.2.3 on 2023-10-12 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alldata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('companyname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('designation', models.CharField(max_length=255)),
                ('purpose', models.CharField(max_length=255)),
                ('report', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='visitor',
            options={'managed': False},
        ),
    ]
