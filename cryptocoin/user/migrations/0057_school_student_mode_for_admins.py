# Generated by Django 2.0.3 on 2018-05-07 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0056_auto_20180503_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='student_mode_for_admins',
            field=models.BooleanField(default=False),
        ),
    ]
