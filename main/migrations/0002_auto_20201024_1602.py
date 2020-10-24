# Generated by Django 3.1.2 on 2020-10-24 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=15)),
                ('color', models.CharField(max_length=15)),
                ('size', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=15)),
                ('sort', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Temp_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_name', models.CharField(max_length=200)),
                ('max_temp', models.FloatField()),
                ('min_temp', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cloth_female',
        ),
        migrations.DeleteModel(
            name='Cloth_male',
        ),
        migrations.AddField(
            model_name='cloth',
            name='temp',
            field=models.ForeignKey(db_column='temp_name', on_delete=django.db.models.deletion.CASCADE, to='main.temp_category'),
        ),
    ]
