from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    path('createstudent/',views.CreateStudent.as_view(), name='create_student'),
    path('liststudent/',views.ListStudent.as_view(), name='list'),
    path('studentdata/', views.studentdata, name='student_data'),
]
