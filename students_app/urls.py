from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # root of students_app
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # root of students_app
]