from django.urls import path
from .views import *
urlpatterns = [
    path('patient/<int:pk>', PatientRetrieveUpdateDestroyView.as_view(), name='update-patient-list'),
    path('patient/',PatientListCreateView.as_view(),name='patient-list'),
    path('patient/<int:stock_id>/price/', PatientDetailView.as_view(), name='patient-price'),

    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDestroyView.as_view(), name='doctor-detail'),

    # Patient-Doctor Mappings
    path('mappings/', MappingListCreateView.as_view(), name='mapping-list-create'),
   # For retrieving mappings by patient ID
    path('mappings/<int:patient_id>/', MappingRetrieveByPatientView.as_view(), name='mappings-by-patient'),

    # For deleting a specific mapping by primary key
    path('mapping/<int:pk>/', MappingDestroyView.as_view(), name='mapping-delete'),

    
]