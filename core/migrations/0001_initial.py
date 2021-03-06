# Generated by Django 3.0.3 on 2020-02-22 00:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proyecto', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('proveedor', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('unidad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(default='empty', upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
