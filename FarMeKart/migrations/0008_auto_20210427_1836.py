# Generated by Django 3.0 on 2021-04-27 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FarMeKart', '0007_auto_20210427_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpro',
            name='e',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FarMeKart.Vegpro'),
        ),
    ]