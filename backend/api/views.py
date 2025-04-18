from rest_framework import filters
from rest_framework.generics import ListAPIView,RetrieveAPIView, get_object_or_404
from .serializers import StudentListSerializer,StudentDetailSerializer
from .models import Student,Batch

class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer

    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['admission_number','university_id','first_name','middle_name','last_name']
    ordering_fields = ['admission_number', 'university_id']
    #Default ordering Scheme
    ordering = ['admission_number']

class StudentDetailAPIView(RetrieveAPIView):
    # No need for queryset as custom object lookup is used
    # queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer

    # Overwrite lookup_fields to contain two attributes
    def get_object(self):
        #Get university_id from the passed url
        university_id = self.kwargs.get('university_id')
        
        #Get year from the passed url

        year = self.kwargs.get('batch')
        
        # Get batch object from year
        # It is passed as 16,17 etc.. on the url but need to pass it as 2016,2020 etc... to the database
        
        batch = get_object_or_404(Batch,year=year+2000)


        return get_object_or_404( Student ,university_id=university_id, batch = batch)

