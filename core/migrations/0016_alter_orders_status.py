# Generated by Django 3.2.12 on 2022-07-20 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20220720_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('1', 'Pending'), ('2', 'Delivered')], default='1', max_length=50),
        ),
    ]
