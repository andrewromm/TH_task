# Generated by Django 5.0 on 2024-01-02 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_cw_performed_cw_created_at_cw_is_deleted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_months',
            field=models.IntegerField(blank=True, verbose_name='Месяцев до повтора задачи'),
        ),
    ]
