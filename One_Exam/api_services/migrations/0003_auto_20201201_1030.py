# Generated by Django 3.0.2 on 2020-12-01 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_services', '0002_auto_20201118_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poc_marks_memo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('std_name', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=300, null=True)),
                ('place', models.CharField(blank=True, max_length=100, null=True)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('grade', models.CharField(blank=True, max_length=1, null=True)),
                ('paper1', models.CharField(blank=True, max_length=100, null=True)),
                ('paper2', models.CharField(blank=True, max_length=100, null=True)),
                ('paper1_marks_required', models.IntegerField(blank=True, null=True)),
                ('paper2_marks_required', models.IntegerField(blank=True, null=True)),
                ('paper1_marks_obtained', models.IntegerField(blank=True, null=True)),
                ('paper2_marks_obtained', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'poc_marks_memo',
            },
        ),
        migrations.AddField(
            model_name='media',
            name='mediasource',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
