from django.urls import include, path
from rest_framework.routers import DefaultRouter

from wfrp.api.views import (CampaignViewSet, JournalEntryViewSet, PlayableCharacterViewSet,
                            ItemViewSet, TalentViewSet, SpellViewSet, ArmourViewSet, WeaponViewSet, AdvancedSkillViewSet)

router = DefaultRouter()
router.register(prefix=r"campaigns",
                viewset=CampaignViewSet,
                basename="campaigns")
router.register(prefix=r"journal-entries",
                viewset=JournalEntryViewSet,
                basename="journal-entries")
router.register(prefix=r"playable-characters",
                viewset=PlayableCharacterViewSet,
                basename="playable-characters")
router.register(prefix=r"items",
                viewset=ItemViewSet,
                basename="items")
router.register(prefix=r"weapons",
                viewset=WeaponViewSet,
                basename="weapons")
router.register(prefix=r"armor",
                viewset=ArmourViewSet,
                basename="armor")
router.register(prefix=r"talents",
                viewset=TalentViewSet,
                basename="talents")
router.register(prefix=r"advanced-skills",
                viewset=AdvancedSkillViewSet,
                basename="advanced-skills")
router.register(prefix=r"spells",
                viewset=SpellViewSet,
                basename="spells")

urlpatterns = [
    path("", include(router.urls)),
]
