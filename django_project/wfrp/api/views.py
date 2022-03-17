from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from wfrp.models import Campaign, JournalEntry
from wfrp.api.serializers import CampaignSerializer, JournalEntrySerializer
from wfrp.api.permissions import IsAuthorOrReadOnly, IsMasterOrReadOnly

class CampaignViewSet(viewsets.ModelViewSet):
    serializer_class = CampaignSerializer
    lookup_field = "uuid"
    queryset = Campaign.objects.all().order_by("-creation_date")
    permission_classes = [IsAuthenticated, IsMasterOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(master=self.request.user)

class JournalEntryViewSet(viewsets.ModelViewSet):
    serializer_class = JournalEntrySerializer
    lookup_field = "uuid"
    queryset = JournalEntry.objects.all().order_by("-creation_date")
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)