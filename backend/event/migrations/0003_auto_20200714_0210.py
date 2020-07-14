# Generated by Django 2.2.14 on 2020-07-14 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20200713_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorites',
            name='user',
        ),
        migrations.RemoveField(
            model_name='favorites',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='myschedule',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='myschedule',
            name='user',
        ),
        migrations.RemoveField(
            model_name='presenter',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='location',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='location',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='category',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='location',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='type',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='website',
        ),
        migrations.RemoveField(
            model_name='vendordetail',
            name='vendor_id',
        ),
        migrations.AddField(
            model_name='favorites',
            name='jk',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myschedule',
            name='pp',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
