from django.shortcuts import render
from django.http import HttpResponse
from student.api.serializers import Studentserializers 
from rest_framework import generics
from rest_framework.response import Response
from student.models import Student
import requests
import json

# Create your views here.

class CreateStudent(generics.CreateAPIView):
    serializer_class = Studentserializers
    queryset = Student.objects.all()
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "status": "success",
            "message": "Student created successfully",
            "data": response.data
        })
        
class ListStudent(generics.ListAPIView):
    serializer_class = Studentserializers
    queryset = Student.objects.all()
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            "status": "success",
            "message": "Student listed successfully",
            "data": response.data
        })
        
def studentdata(request):
    try: 
        response = requests.get('http://127.0.0.1:8000/student/liststudent/')
        data = response.json()
        data = data["data"]
        print(7777,data)
    except requests.RequestException as e:
            data = {'error':str(e)}
    except ValueError as e:
        data = {'error':f"Error parsing JSON response: {e}"}
            
    return render(request,'studentdata.html',{'data':data})
    


