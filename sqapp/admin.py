from django.contrib import admin
from .models import Quiz, Question, Answer, UserProfile, UserAnswer
# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserProfile)
admin.site.register(UserAnswer)