# Generated by Django 3.2.5 on 2021-07-16 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
    ]