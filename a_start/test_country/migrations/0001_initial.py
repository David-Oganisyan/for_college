# Generated by Django 4.1.5 on 2023-02-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='For_teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='имя')),
                ('surname', models.CharField(max_length=200, verbose_name='фамилия')),
                ('course', models.CharField(max_length=200, verbose_name='курс')),
                ('college', models.CharField(max_length=500, verbose_name='колледж')),
                ('subject', models.CharField(max_length=1000, verbose_name='предмет')),
                ('delivery_time', models.DateTimeField(auto_now_add=True, verbose_name='время сдачи')),
                ('question_1', models.BooleanField(default=False, verbose_name='вопрос_1')),
                ('question_2', models.BooleanField(default=False, verbose_name='вопрос_2')),
                ('question_3', models.BooleanField(default=False, verbose_name='вопрос_3')),
                ('question_4', models.BooleanField(default=False, verbose_name='вопрос_4')),
                ('question_5', models.BooleanField(default=False, verbose_name='вопрос_5')),
                ('count', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'студент',
                'verbose_name_plural': 'студенты',
            },
        ),
    ]
