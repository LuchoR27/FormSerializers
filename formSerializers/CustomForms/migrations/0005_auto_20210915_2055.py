# Generated by Django 3.2.7 on 2021-09-15 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CustomForms', '0004_auto_20210915_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='actions',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='condition',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='conditional_widget',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variable_widgets', to='CustomForms.widget'),
        ),
    ]
