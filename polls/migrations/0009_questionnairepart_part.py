# Generated by Django 3.0.8 on 2020-07-07 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20200704_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnairepart',
            name='part',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='polls.Part'),
        ),
    ]
