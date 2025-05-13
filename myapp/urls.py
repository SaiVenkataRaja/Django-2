from django.urls import path 
from . import views
urlpatterns = [
    # path('', views.home, name='home'),
    path('student/', views.student_form_view, name='student_form'),
    path('students/', views.student_list_view, name='student_list'),
    path('student/<int:id>/edit', views.edit_student, name="edit_student"),
    path('student/<int:id>/delete', views.delete_student, name="delete_student"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
] 
