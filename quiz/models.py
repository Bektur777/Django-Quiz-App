from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Имя', max_length=25)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Quiz(models.Model):
    title = models.CharField('Название', max_length=25)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    text = models.TextField('Вопрос')
    question_quiz = models.ForeignKey(Quiz, related_name='question', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    text = models.TextField('Ответ')
    draft = models.BooleanField(default=False)
    quiz_answer = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

