# Generated by Django 4.0 on 2022-09-03 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_remove_answer_slug_remove_question_answer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_quiz',
        ),
        migrations.AddField(
            model_name='quiz',
            name='question_quiz',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='quiz.question'),
        ),
    ]
