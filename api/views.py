from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from api.models import Expense
from api.serializers import ExpenseSerializer
from api.permissions import IsOwnerOrReadOnly, IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from .filters import FilterPubDate

class ApiViewsets(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsOwner]
    filter_backends = [DjangoFilterBackend]
    # ordering_fields = ['pub_date']  
    filterset_class = FilterPubDate
    
    def get_queryset(self):
        return Expense.objects.filter(owner = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    