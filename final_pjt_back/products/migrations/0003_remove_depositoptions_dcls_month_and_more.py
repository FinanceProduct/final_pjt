# Generated by Django 4.2.1 on 2023-05-23 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_depositproducts_dcls_month"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="depositoptions",
            name="dcls_month",
        ),
        migrations.RemoveField(
            model_name="depositproducts",
            name="dcls_month",
        ),
    ]
