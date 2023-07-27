from django.test import TestCase
from student.models import Student
from datetime import datetime

# Create your tests here.
class StudentModelTestCase(TestCase):
    def test_student_creation(self):
        payload = {
            'name' : "google",
            'roll' : 1,
           
            'slug' : "test",
           
            'dob' : datetime(2021,2,3),
            'phone_number' : "test",
           
            'image_url' : "test"
        }
            
        
        student = Student.objects.create(**payload)
           
        
        saved_student = Student.objects.get(pk = student.pk)
        
        self.assertEqual(saved_student.name, payload['name'])
        self.assertEqual(saved_student.roll, payload['roll'])
       
        self.assertEqual(saved_student.slug,payload['slug'])
        self.assertEqual(saved_student.dob,payload['dob'].date())
        self.assertEqual(saved_student.phone_number,payload['phone_number'])
        self.assertEqual(saved_student.image_url, payload['image_url'])
        
