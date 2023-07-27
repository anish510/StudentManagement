from django.shortcuts import render
from django.http import HttpResponse
from teacher.api.serializers import TeacherSerializers
from rest_framework import generics
from rest_framework.response import Response
from teacher.models import Teacher
import requests
import json

# Create your views here.

class CreateTeacher(generics.CreateAPIView):
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "status": "success",
            "message": "Teacher created successfully",
            "data": response.data
        })

class ListTeacher(generics.ListAPIView):
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            "status": "success",
            "message": "Teacher listed successfully",
            "data": response.data
        })
        
def teacherdata(request):
    try: 
        response = requests.get('http://127.0.0.1:8000/teacher/listteacher/')
        data = response.json()
        data = data['data']
    except requests.RequestException as e:
            data = {'error':str(e)}
    except ValueError as e:
        data = {'error':f"Error parsing JSON response: {e}"}
            
    return render(request,'teachersdata.html',{'data':data})
            