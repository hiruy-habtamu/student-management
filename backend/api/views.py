from rest_framework import filters
from rest_framework.generics import ListAPIView
from .serializers import StudentListSerializer
from .models import Student

class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['admission_number','university_id','first_name','middle_name','last_name']
    ordering_fields = ['admission_number', 'university_id']
    #Default ordering Scheme
    ordering = ['admission_number']
