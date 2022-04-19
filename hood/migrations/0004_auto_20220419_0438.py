# Generated by Django 3.2.9 on 2022-04-19 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_auto_20220418_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='health_center',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='health_contact',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='health_email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='Health',
        ),
    ]
