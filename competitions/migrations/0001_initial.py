# Generated by Django 3.1 on 2020-08-28 15:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competitions',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('age_group', models.TextField()),
                ('rank', models.TextField()),
            ],
            options={
                'db_table': 'competitions',
            },
        ),
        migrations.CreateModel(
            name='Referees',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('referee_uuid', models.UUIDField()),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.competitions')),
            ],
            options={
                'db_table': 'referees',
            },
        ),
        migrations.CreateModel(
            name='Competitors',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('couple_uuid', models.UUIDField()),
                ('points', models.IntegerField(default=0)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.competitions')),
            ],
            options={
                'db_table': 'competitors',
            },
        ),
    ]
