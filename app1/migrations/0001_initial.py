# Generated by Django 4.1.4 on 2023-03-20 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Muaji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mauji', models.CharField(max_length=20)),
                ('sfida', models.CharField(max_length=256)),
            ],
        ),
    ]
