# Generated by Django 2.2.4 on 2019-12-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.DecimalField(decimal_places=2, max_digits=10)),
                ('humedad', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]