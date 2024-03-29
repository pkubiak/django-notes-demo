# Generated by Django 2.2.7 on 2019-11-27 21:36

from django.db import migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_note_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'get_latest_by': 'modified', 'ordering': ('-modified', '-created')},
        ),
        migrations.RemoveField(
            model_name='note',
            name='published_at',
        ),
        migrations.AddField(
            model_name='note',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]
