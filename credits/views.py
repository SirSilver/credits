from django.shortcuts import render
from rest_framework import viewsets
from .models import Application, Blacklist, Borrower, Program
from .serializers import ApplicationSerializer, BlacklistSerializer, BorrowerSerializer, ProgramSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    """Viewset for listing, retrieving, creating, updating and deleting programs"""
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class BorrowerViewSet(viewsets.ModelViewSet):
    """Viewset for listing, retrieving, creating, updating and deleting borrowers"""
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    """Viewset for listing, retrieving, creating, updating and deleting applications"""
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class BlacklistView(viewsets.ReadOnlyModelViewSet):
    """Viewset for viewing blacklist"""
    queryset = Blacklist.objects.all()
    serializer_class = BlacklistSerializer
