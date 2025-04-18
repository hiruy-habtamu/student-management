from rest_framework import serializers
from .models import Student,Dorm

class DormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dorm
        exclude = ['id']
class StudentListSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='student-detail',read_only=True)
    class Meta:
        model = Student
        fields = ['admission_number','university_id','first_name','middle_name','last_name','section','link']
        

class StudentDetailSerializer(serializers.ModelSerializer):
    batch = serializers.CharField(source='batch.year')
    dorm = DormSerializer()
    class Meta:
        model = Student
        fields = '__all__'
