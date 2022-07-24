# Generated by Django 4.0.6 on 2022-07-24 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(max_length=100, unique=True)),
                ('total_cost_order', models.FloatField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetailComputer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost_order', models.FloatField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.computer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.order')),
            ],
        ),
    ]
