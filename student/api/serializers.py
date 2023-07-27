from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from student.models import Student

class Studentserializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'name',
            'roll',
            'city',
            'dob',
            'phone_number',
            'image_url',
            ]
        
    