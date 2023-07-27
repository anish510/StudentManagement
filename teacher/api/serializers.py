from rest_framework import serializers
from teacher.models import Teacher

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            'name',
            'image_url',
            'position',
            'phone_number',
            'email'
        ]