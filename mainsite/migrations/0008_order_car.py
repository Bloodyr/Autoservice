# Generated by Django 4.1.3 on 2022-11-23 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0007_alter_clientauto_client_alter_order_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='car',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainsite.clientauto', verbose_name='Машина клиента'),
        ),
    ]
