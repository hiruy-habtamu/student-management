from rest_framework import serializers
from .models import Student

class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['admission_number','university_id','first_name','middle_name','last_name']
        read_only_fields = fields
    