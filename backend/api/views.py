from rest_framework import filters
from rest_framework.generics import ListAPIView,RetrieveAPIView, get_object_or_404
from .serializers import StudentListSerializer,StudentDetailSerializer
from .models import Student,Batch
from rest_framework.permissions import BasePermission,IsAdminUser,IsAuthenticated

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        # Check if the request maker's user instance is associated with the one he is asking for in the urls.py
        university_id = view.kwargs.get('university_id')
        year = view.kwargs.get('batch')
        batch = get_object_or_404(Batch,year=year+2000)
        return request.user.id == Student.objects.get(university_id = university_id,batch=batch).user_id
         
class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['admission_number','university_id','first_name','middle_name','last_name']
    ordering_fields = ['admission_number', 'university_id']
    #Default ordering Scheme
    ordering = ['admission_number']

class StudentDetailAPIView(RetrieveAPIView):
    # No need for queryset as custom object lookup is used
    # queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer
    permission_classes = [IsOwner|IsAdminUser]
    

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

