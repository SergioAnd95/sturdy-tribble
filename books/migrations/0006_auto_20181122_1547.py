# Generated by Django 2.1.3 on 2018-11-22 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20181120_1334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('-published_date', '-pk')},
        ),
    ]
