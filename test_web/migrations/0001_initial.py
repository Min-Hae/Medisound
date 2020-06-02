# Generated by Django 3.0.6 on 2020-05-23 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=20)),
                ('effect', models.TextField()),
                ('use', models.TextField()),
            ],
            options={
                'ordering': ['id', 'name'],
            },
        ),
    ]
