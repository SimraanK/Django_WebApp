# Generated by Django 4.1.2 on 2022-11-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_alter_contact_email_alter_contact_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="phone",
            field=models.DecimalField(decimal_places=12, max_digits=12),
        ),
    ]
