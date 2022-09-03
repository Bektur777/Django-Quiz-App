from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['text', 'draft']
    list_editable = ['draft', ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'answer']


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    save_as = True
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
