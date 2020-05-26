# Generated by Django 3.0 on 2020-05-26 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20200513_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='allstudent',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='studentphoto'),
        ),
        migrations.AlterField(
            model_name='examscore',
            name='subject',
            field=models.CharField(choices=[('คณิตศาสตร์', 'math'), ('วิทยาศาสตร์', 'วิทยาศาสตร์'), ('ศิลป', 'ศิลป'), ('อังกฤษ', 'ภาษาอังกฤษ'), ('ฟิสิกส์', 'ฟิสิกส์'), ('ชีววิทยา', 'ชีววิทยา')], default='คณิตศาสตร์', max_length=200),
        ),
    ]