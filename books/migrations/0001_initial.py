# Generated by Django 2.1.3 on 2018-11-19 18:48

from django.db import migrations, models
import isbn_field.fields
import isbn_field.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('authors_info', models.TextField()),
                ('isbn', isbn_field.fields.ISBNField(max_length=28, unique=True, validators=[isbn_field.validators.ISBNValidator], verbose_name='ISBN')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
