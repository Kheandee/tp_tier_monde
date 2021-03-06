# Generated by Django 3.1.1 on 2022-03-23 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_artist', models.CharField(max_length=50)),
                ('skill_artist', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_event', models.CharField(max_length=50)),
                ('av_ticket', models.IntegerField(blank=True, null=True)),
                ('begin_date', models.DateTimeField(verbose_name="Date de début d'event")),
                ('end_date', models.DateTimeField(verbose_name="Date de fin d'event")),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HallCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_material', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_user', models.CharField(max_length=50)),
                ('firstname_user', models.CharField(max_length=50)),
                ('mail_user', models.CharField(max_length=50)),
                ('pwd_user', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Halls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_hall', models.CharField(max_length=50)),
                ('size_hall', models.BigIntegerField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.events')),
                ('hall_category', models.ManyToManyField(to='event.HallCategory')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.material')),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_group', models.CharField(max_length=50)),
                ('type_group', models.CharField(max_length=50)),
                ('artist', models.ManyToManyField(to='event.Artist')),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='group',
            field=models.ManyToManyField(to='event.Groups'),
        ),
        migrations.AddField(
            model_name='events',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.eventtype'),
        ),
        migrations.AddField(
            model_name='events',
            name='user',
            field=models.ManyToManyField(to='event.Users'),
        ),
    ]
