# Generated by Django 5.1.1 on 2024-11-02 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_transaction_transfared_user_account_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transfared_user_account_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
