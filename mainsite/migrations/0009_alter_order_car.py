# Generated by Django 4.1.3 on 2022-11-23 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0008_order_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.clientauto', verbose_name='Машина клиента'),
        ),
    ]