from applications.questions.forms import QuestionForm
from django.contrib import admin
from .models import Question


# Register your models here.

admin.site.register(Question)
