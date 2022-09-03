from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['text', 'draft']
    list_editable = ['draft', ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text']
    inlines = [AnswerInline]


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    inlines = [QuestionInline]
    prepopulated_fields = {'slug': ('title',)}


admin.site.site_title = 'Django Quiz App'
admin.site.site_header = 'Django Quiz App'
