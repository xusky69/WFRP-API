from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from wfrp.models import Campaign
from wfrp.api.serializers import CampaignSerializer
from wfrp.api.permissions import IsAuthorOrReadOnly

class CampaignViewSet(viewsets.ModelViewSet):
    serializer_class = CampaignSerializer
    lookup_field = "uuid"
    queryset = Campaign.objects.all().order_by("-creation_date")
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(master=self.request.user)
