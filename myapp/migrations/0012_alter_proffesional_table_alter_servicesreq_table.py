# Generated by Django 4.1.7 on 2023-08-10 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_rename_users_usr_alter_usr_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='proffesional',
            table='proffesional_detail',
        ),
        migrations.AlterModelTable(
            name='servicesreq',
            table='service_detail',
        ),
    ]
