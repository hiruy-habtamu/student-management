from rest_framework import serializers
from .models import Student,Dorm

class DormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dorm
        exclude = ['id']
class StudentListSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = ['admission_number','university_id','first_name','middle_name','last_name','section','link']

    def get_link(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(
            # Need to display batch as two digit number
            f"/students/{obj.university_id}/{int(str(obj.batch.year)[-2:])}"
        )

class StudentDetailSerializer(serializers.ModelSerializer):
    batch = serializers.CharField(source='batch.year')
    dorm = DormSerializer()
    class Meta:
        model = Student
        fields = '__all__'
