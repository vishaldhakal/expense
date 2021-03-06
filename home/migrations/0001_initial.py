# Generated by Django 3.1 on 2020-09-30 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='creditTaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=500)),
                ('details', models.CharField(blank=True, max_length=500)),
                ('total_due', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('amount', models.CharField(choices=[('paid', 'paid'), ('credit', 'credit')], max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('credit_taker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.credittaker')),
            ],
        ),
    ]
