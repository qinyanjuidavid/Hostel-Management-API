# Generated by Django 3.2.9 on 2022-07-03 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('hostel', '0003_alter_space_vacant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostelbooking',
            name='student',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.student'),
        ),
    ]