# Generated by Django 3.0.5 on 2020-04-10 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Forum', '0003_auto_20200408_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='Pub_User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
