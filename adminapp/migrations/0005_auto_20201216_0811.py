# Generated by Django 2.2.17 on 2020-12-16 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_auto_20201216_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paket',
            name='jml_pertemuan',
            field=models.CharField(blank=True, choices=[(1, '1X Pertemuan'), (2, '2X Pertemuan'), (3, '3X Pertemuan'), (4, '4X Pertemuan')], max_length=200, null=True),
        ),
    ]