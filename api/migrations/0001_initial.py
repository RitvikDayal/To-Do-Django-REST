# Generated by Django 3.1.1 on 2020-09-04 11:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=150)),
                ('task_detail', models.TextField(blank=True, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('schedule_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]