# Generated by Django 4.1.1 on 2022-09-12 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=227)),
                ('email', models.CharField(max_length=227)),
                ('gender', models.CharField(max_length=227)),
                ('blood', models.CharField(max_length=227)),
                ('is_active', models.BooleanField()),
            ],
        ),
    ]
