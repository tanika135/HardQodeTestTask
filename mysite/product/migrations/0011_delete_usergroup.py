# Generated by Django 5.0.2 on 2024-03-02 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_group_user_product_max_users_product_min_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserGroup',
        ),
    ]