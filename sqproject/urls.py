from django.contrib import admin
from django.urls import path, include
from sqapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('login/', views.logger, name='logger'),
    path('closelog/', views.closelog, name='closelog'),
    path('test/<int:quiz_id>/', views.show_quiz, name='show_quiz'),
    path('answer_process/', views.answer_process, name='answer_process'),
    path('done/', views.done, name='done'),
    path('profile/', views.profile, name = 'profile'),
]
