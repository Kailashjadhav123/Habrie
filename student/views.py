from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdateView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'


class StudentDeleteView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    lookup_field = 'id' 

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)