from .models import Poryect
from rest_framework import viewsets, permissions
from .serializers import ProyectSerializer

class ProyectViewSet(viewsets.ModelViewSet):
    queryset = Poryect.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProyectSerializer
