# Generated by Django 2.1.2 on 2019-06-28 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0083_auto_20190628_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='honory_coins',
            field=models.BigIntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='permanent_coins',
            field=models.BigIntegerField(default=0),
        ),
    ]