# Generated by Django 3.2.6 on 2021-08-15 15:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_alter_cards_code_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='publish_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]