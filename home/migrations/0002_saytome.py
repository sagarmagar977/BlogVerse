# Generated by Django 4.2.3 on 2023-07-15 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SayToMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_is', models.CharField(blank=True, max_length=180, null=True)),
                ('saying', models.TextField()),
            ],
        ),
    ]
