# Generated by Django 2.1.2 on 2019-06-24 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0080_userdata_group_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketitem',
            name='description',
            field=models.CharField(default='-', max_length=400),
        ),
        migrations.AlterField(
            model_name='marketitem',
            name='name',
            field=models.CharField(default='-', max_length=100),
        ),
    ]
