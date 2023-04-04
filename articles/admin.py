from django.contrib import admin
from .models import CategoryQuestions, Questions, Interviews


admin.site.register(Questions)
admin.site.register(CategoryQuestions)
admin.site.register(Interviews)
