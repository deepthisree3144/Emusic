# Generated by Django 5.1.4 on 2024-12-13 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='r_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=20)),
                ('Age', models.IntegerField(default='', max_length=5)),
                ('Adress', models.CharField(default='', max_length=50)),
                ('Contact', models.IntegerField(default='', max_length=10)),
                ('Mail', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
