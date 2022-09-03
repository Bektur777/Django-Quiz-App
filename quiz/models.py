from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField('Имя', max_length=25)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Answer(models.Model):
    text = models.TextField('Ответ')
    draft = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Question(models.Model):
    title = models.CharField('Название', max_length=25)
    question = models.TextField('Вопрос')
    answer = models.ForeignKey(Answer, related_name='answer', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Quiz(models.Model):
    title = models.CharField('Название', max_length=25)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
    slug = models.BooleanField(max_length=25, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
