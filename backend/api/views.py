from rest_framework import filters
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .serializers import StudentListSerializer,StudentDetailSerializer
from .models import Student

class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['admission_number','university_id','first_name','middle_name','last_name']
    ordering_fields = ['admission_number', 'university_id']
    #Default ordering Scheme
    ordering = ['admission_number']

class StudentDetailAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer

