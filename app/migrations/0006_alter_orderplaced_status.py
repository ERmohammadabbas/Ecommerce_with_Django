# Generated by Django 5.0.4 on 2024-09-04 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Deliverd', 'Deliverd'), ('Cancel', 'Cancel'), ('Pending', 'Pending')], default='Pending', max_length=50),
        ),
    ]
