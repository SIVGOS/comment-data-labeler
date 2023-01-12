# Generated by Django 2.2.11 on 2023-01-12 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=16)),
                ('topic', models.CharField(max_length=32)),
                ('channel_title', models.CharField(max_length=32)),
                ('video_title', models.CharField(max_length=128)),
                ('comment_id', models.CharField(max_length=32)),
                ('comment_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Labels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_text', models.CharField(max_length=64, unique=True)),
                ('display_text', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='LabellerMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeler.Comment')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeler.Labels')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='labels',
            field=models.ManyToManyField(to='labeler.Labels'),
        ),
    ]
