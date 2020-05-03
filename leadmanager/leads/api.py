from rest_framework import viewsets, permissions

from .models import Lead
from .serializers import LeadSerializer


# Lead ViewSet
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer
