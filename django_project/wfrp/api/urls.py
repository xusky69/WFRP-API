from django.urls import include, path
from rest_framework.routers import DefaultRouter
from wfrp.api.views import (AdvancedSkillViewSet, ArmourViewSet,
                            CampaignViewSet, CreatureTraitViewSet,
                            CreatureViewSet, ItemViewSet, JournalEntryViewSet,
                            MemoryViewSet, PlayableCharacterViewSet,
                            SpellViewSet, TalentViewSet, WeaponViewSet)

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
router.register(prefix=r"memories",
                viewset=MemoryViewSet,
                basename="memories")
router.register(prefix=r"creatures",
                viewset=CreatureViewSet,
                basename="creatures")
router.register(prefix=r"creature-traits",
                viewset=CreatureTraitViewSet,
                basename="creature-traits")

urlpatterns = [
    path("", include(router.urls)),
]

