# Generated by Django 4.0 on 2021-12-25 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_chart', '0003_testchart_testchart_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chart_data',
            name='chart',
        ),
        migrations.RemoveField(
            model_name='chart_data',
            name='user',
        ),
        migrations.DeleteModel(
            name='CHART',
        ),
        migrations.DeleteModel(
            name='CHART_DATA',
        ),
    ]
