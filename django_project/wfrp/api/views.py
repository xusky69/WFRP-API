from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from wfrp.api.permissions import IsAuthorOrReadOnly, IsMasterOrReadOnly
from wfrp.api.serializers import (CampaignSerializer, ItemSerializer,
                                  JournalEntrySerializer,
                                  PlayableCharacterSerializer, SpellSerializer,
                                  TalentSerializer)
from wfrp.models import (Campaign, Item, JournalEntry, PlayableCharacter,
                         Spell, Talent)

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
    filterset_fields = ('campaign__uuid',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PlayableCharacterViewSet(viewsets.ModelViewSet):
    serializer_class = PlayableCharacterSerializer
    lookup_field = "uuid"
    queryset = PlayableCharacter.objects.all().order_by("-creation_date")
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    filterset_fields = ('campaign__uuid','user__username')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TalentViewSet(viewsets.ModelViewSet):
    serializer_class = TalentSerializer
    lookup_field = "uuid"
    queryset = Talent.objects.all().order_by("-creation_date")
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    lookup_field = "uuid"
    queryset = Item.objects.all().order_by("-creation_date")
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SpellViewSet(viewsets.ModelViewSet):
    serializer_class = SpellSerializer
    lookup_field = "uuid"
    queryset = Item.objects.all().order_by("-creation_date")
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
