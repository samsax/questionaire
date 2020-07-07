# Generated by Django 3.0.8 on 2020-07-05 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_partquestionnaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='questionnaire',
        ),
        migrations.AlterField(
            model_name='partquestionnaire',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.Question'),
        ),
    ]
