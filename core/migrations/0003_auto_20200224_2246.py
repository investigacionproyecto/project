# Generated by Django 3.0.3 on 2020-02-24 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_boleto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleto',
            name='fecha_nacimiento',
            field=models.DateTimeField(),
        ),
    ]
