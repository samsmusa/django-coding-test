# Generated by Django 4.0.6 on 2022-07-21 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_productvariant_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pvarinat', to='product.product'),
        ),
    ]
