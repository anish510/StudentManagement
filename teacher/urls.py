from django.urls import path
from . import views


app_name = 'teacher'
urlpatterns = [
    path('createteacher/',views.CreateTeacher.as_view(),name='create_teacher'),
    path('listteacher/',views.ListTeacher.as_view(), name = 'list_teacher'),
    path('teachersdata/',views.teacherdata,name='teacherdata'),
    
    
]
