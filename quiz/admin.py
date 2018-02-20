from django.contrib import admin
from .models import Question, Answer, Quiz



class QuestionAdmin(Question):
    list_display = ('id')


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quiz)
