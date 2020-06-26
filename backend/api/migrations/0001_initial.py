# Generated by Django 3.0.7 on 2020-06-12 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'form',
            },
        ),
        migrations.CreateModel(
            name='HealthFacility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'healthfacility',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to='upload_location')),
                ('year', models.CharField(max_length=5)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form', to='api.Form')),
                ('healthfacility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='healthfacility', to='api.HealthFacility')),
            ],
            options={
                'db_table': 'image',
            },
        ),
    ]
