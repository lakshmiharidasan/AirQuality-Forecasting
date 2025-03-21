# Generated by Django 5.1.5 on 2025-02-18 16:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alert_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='experttbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('Post', models.CharField(max_length=100)),
                ('mobileno', models.BigIntegerField(max_length=10)),
                ('place', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='logintbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('pasword', models.CharField(max_length=200)),
                ('utype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dataset_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=400)),
                ('answer', models.CharField(max_length=400)),
                ('date', models.DateField()),
                ('EXPERT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.experttbl')),
            ],
        ),
        migrations.AddField(
            model_name='experttbl',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.logintbl'),
        ),
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('EXPERT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.experttbl')),
            ],
        ),
        migrations.CreateModel(
            name='tips_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tips', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('EXPERT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.experttbl')),
            ],
        ),
        migrations.CreateModel(
            name='usertbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('mobileno', models.BigIntegerField(max_length=10)),
                ('place', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.logintbl')),
            ],
        ),
        migrations.CreateModel(
            name='feedbacktbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('USERID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usertbl')),
            ],
        ),
    ]
