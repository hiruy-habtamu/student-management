from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from .views import StudentListAPIView,StudentDetailAPIView
urlpatterns = [

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    path('students/',StudentListAPIView.as_view()),
    path('students/<int:university_id>/<int:batch>',StudentDetailAPIView.as_view(),name="student-detail")
]