# Generated by Django 3.0.4 on 2020-03-25 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=256),
        ),
    ]
