from django.urls import include, path
from rest_framework.routers import DefaultRouter

from wfrp.api.views import CampaignViewSet, JournalEntryViewSet, PlayableCharacterViewSet

router = DefaultRouter()
router.register(prefix=r"campaigns", 
                viewset=CampaignViewSet, 
                basename = "campaigns")
router.register(prefix=r"journal-entries", 
                viewset=JournalEntryViewSet, 
                basename = "journal-entries")
router.register(prefix=r"playable-characters", 
                viewset=PlayableCharacterViewSet, 
                basename = "playable-characters")

urlpatterns = [
    path("", include(router.urls)),
]