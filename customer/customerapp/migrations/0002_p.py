# Generated by Django 3.0.5 on 2020-04-12 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='p',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=10)),
                ('productId', models.IntegerField()),
            ],
        ),
    ]
