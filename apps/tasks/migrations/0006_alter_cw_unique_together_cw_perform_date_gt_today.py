# Generated by Django 5.0 on 2024-01-03 20:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_cw_next_due_date'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cw',
            unique_together={('task', 'perform_date')},
        ),
        migrations.AddConstraint(
            model_name='cw',
            constraint=models.CheckConstraint(check=models.Q(('perform_date__lte', datetime.date(2024, 1, 3))), name='perform_date_gt_today'),
        ),
    ]
