# Generated by Django 2.0.7 on 2018-07-27 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omautotest', '0002_auto_20180727_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streetexecutionreport',
            name='Price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='streetexecutionreport',
            name='Qty',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]