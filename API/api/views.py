from rest_framework import viewsets

from .models import Ticket
from .serializer import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
