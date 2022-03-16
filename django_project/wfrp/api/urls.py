from django.urls import include, path
from rest_framework.routers import DefaultRouter

from wfrp.api.views import CampaignViewSet

router = DefaultRouter()
router.register(prefix=r"campaigns", 
                viewset=CampaignViewSet, 
                basename = "campaigns")

urlpatterns = [
    path("", include(router.urls)),
    # path("questions/<slug:slug>/answer", qv.AnswerCreateAPIView.as_view(), name="answer-create"),
    # path("questions/<slug:slug>/answers", qv.AnswerListAPIView.as_view(),name='answer-list'),
    # path("answers/<uuid:uuid>/like", qv.AnswerLikeAPIView.as_view(),name='answer-like'),
    # path("answers/<uuid:uuid>", qv.AnswerRUDAPIView.as_view(),name='answer-detail'),
]