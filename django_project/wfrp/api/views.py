from rest_framework import viewsets
from wfrp.api.permissions import IsAuthorOrReadOnly, IsMasterOrReadOnly
from wfrp.api.serializers import (AdvancedSkillSerializer, ArmourSerializer,
                                  CampaignSerializer, CreatureSerializer,
                                  CreatureTraitSerializer, ItemSerializer,
                                  JournalEntrySerializer, MemorySerializer,
                                  PlayableCharacterSerializer, SpellSerializer,
                                  TalentSerializer, WeaponSerializer)
from wfrp.models import (AdvancedSkill, Armour, Campaign, Creature,
                         CreatureTrait, Item, JournalEntry, Memory,
                         PlayableCharacter, Spell, Talent, Weapon)


class CampaignViewSet(viewsets.ModelViewSet):
    serializer_class = CampaignSerializer
    lookup_field = "uuid"
    queryset = Campaign.objects.all().order_by("-creation_date")
    permission_classes = [IsMasterOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(master=self.request.user)


class JournalEntryViewSet(viewsets.ModelViewSet):
    serializer_class = JournalEntrySerializer
    lookup_field = "uuid"
    queryset = JournalEntry.objects.all().order_by("-creation_date")
    permission_classes = [IsAuthorOrReadOnly]
    filterset_fields = ('campaign__uuid',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PlayableCharacterViewSet(viewsets.ModelViewSet):
    serializer_class = PlayableCharacterSerializer
    lookup_field = "uuid"
    queryset = PlayableCharacter.objects.all().order_by("-creation_date")
    permission_classes = [IsAuthorOrReadOnly]
    filterset_fields = ('campaign__uuid', 'user__username')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TalentViewSet(viewsets.ModelViewSet):
    serializer_class = TalentSerializer
    lookup_field = "uuid"
    queryset = Talent.objects.all().order_by("-creation_date")
    permission_classes = [IsAuthorOrReadOnly]
    filterset_fields = ('character__uuid',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AdvancedSkillViewSet(viewsets.ModelViewSet):
    serializer_class = AdvancedSkillSerializer
    lookup_field = "uuid"
    queryset = AdvancedSkill.objects.all().order_by("-creation_date")
    permission_classes = [IsAuthorOrReadOnly]
    filterset_fields = ('character__uuid',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    lookup_field = "uuid"
    queryset = Item.objects.all().order_by("-creation_date")
    permission_classes = [IsAuthorOrReadOnly]
    filterset_fields = ('character__uuid',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ArmourViewSet(viewsets.ModelViewSet):
    serializer_class = ArmourSerializer
    lookup_field = "uuid"
    queryset = Armour.objects.all().order_by("-creation_date")
    permission_classes = [IsAuthorOrReadOnly]
    filterset_fields = ('character__uuid',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WeaponViewSet(viewsets.ModelViewSet):
    serializer_class = WeaponSerializer
    lookup_field = "uuid"
    queryset = Weapon.objects.all().order_by("-creation_date")
    permission_classes = [IsAuthorOrReadOnly]
    filterset_fields = ('character__uuid',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SpellViewSet(viewsets.ModelViewSet):
    serializer_class = SpellSerializer
    lookup_field = "uuid"
    queryset = Spell.objects.all().order_by("-creation_date")
    permission_classes = [IsAuthorOrReadOnly]
    filterset_fields = ('character__uuid',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MemoryViewSet(viewsets.ModelViewSet):
    serializer_class = MemorySerializer
    lookup_field = "uuid"
    queryset = Memory.objects.all().order_by("-creation_date")
    permission_classes = [IsAuthorOrReadOnly]
    filterset_fields = ('campaign__uuid',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreatureViewSet(viewsets.ModelViewSet):
    serializer_class = CreatureSerializer
    lookup_field = "uuid"
    queryset = Creature.objects.all().order_by("-creation_date")
    permission_classes = [IsAuthorOrReadOnly]
    filterset_fields = ('campaign__uuid',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreatureTraitViewSet(viewsets.ModelViewSet):
    serializer_class = CreatureTraitSerializer
    lookup_field = "uuid"
    queryset = CreatureTrait.objects.all().order_by("-creation_date")
    permission_classes = [IsAuthorOrReadOnly]
    filterset_fields = ('campaign__uuid',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
