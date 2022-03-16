from rest_framework import serializers
from wfrp.models import Campaign

class CampaignSerializer(serializers.ModelSerializer):
    master = serializers.StringRelatedField()

    class Meta:
        model = Campaign
        exclude = ['id'] ### , 'uuid']