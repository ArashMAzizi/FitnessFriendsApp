# Generated by Django 3.1.7 on 2021-04-18 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamifi', '0015_auto_20210418_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisechoice',
            name='category',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='exercisechoice',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exercisechoice',
            name='image_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='exercisechoice',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]