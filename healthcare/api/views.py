from .models import Patient, Doctor, Mapping
from .serializers import PatientSerializer, DoctorSerializer, MappingSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from account.renderers import UserRenderer
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer

class PatientListCreateView(generics.ListCreateAPIView):
    """
    Handles listing stocks for the logged-in user and creating new stocks.
    """
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return stocks associated with the logged-in user
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the stock with the logged-in user
        serializer.save(user=self.request.user)

class PatientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, or deleting a specific Patient for the logged-in user.
    """

    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    renderer_classes = [UserRenderer]

    def get_queryset(self):
        # Return stocks owned by the logged-in user
        return Patient.objects.filter(user=self.request.user)
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Patient deleted successfully."}, status=status.HTTP_200_OK)

class PatientDetailView(APIView):
    """
    Handles retrieving a specific stock's details.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, stock_id):
        try:
            stock = Patient.objects.get(id=stock_id, user=request.user)
            serializer = PatientSerializer(stock)
            return Response(serializer.data)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found."}, status=status.HTTP_404_NOT_FOUND)
        
class DoctorListCreateView(generics.ListCreateAPIView):
    """
    POST /api/doctors/ - Add a new doctor
    GET /api/doctors/  - Retrieve all doctors
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]


class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /api/doctors/<id>/    - Get details of a doctor
    PUT /api/doctors/<id>/    - Update doctor details
    DELETE /api/doctors/<id>/ - Delete a doctor record
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    renderer_classes = [UserRenderer]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Doctor deleted successfully."}, status=status.HTTP_200_OK)

class MappingListCreateView(generics.ListCreateAPIView):
    """
    POST /api/mappings/ - Assign a doctor to a patient
    GET /api/mappings/  - Retrieve all mappings
    """
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]


class MappingRetrieveByPatientView(APIView):
    """
    GET /api/mappings/<patient_id>/ - Get all doctors assigned to a specific patient
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, patient_id):
        mappings = Mapping.objects.filter(patient_id=patient_id)
        serializer = MappingSerializer(mappings, many=True)
        return Response(serializer.data)


class MappingDestroyView(generics.DestroyAPIView):
    """
    DELETE /api/mappings/<id>/ - Remove a doctor from a patient
    """
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Mapping deleted successfully."}, status=status.HTTP_200_OK)


