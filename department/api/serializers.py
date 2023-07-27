from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from department.models import Department

class Departmentserializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            'name',
            'hod',
            ]