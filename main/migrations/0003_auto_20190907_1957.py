# Generated by Django 2.2.5 on 2019-09-07 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_voucher_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='uses',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='discount',
            field=models.CharField(max_length=3),
        ),
    ]