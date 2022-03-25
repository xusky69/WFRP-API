from rest_framework import serializers
from wfrp.models import (Campaign, Item, JournalEntry, PlayableCharacter,
                         Spell, Talent)


class CampaignSerializer(serializers.ModelSerializer):
    master = serializers.StringRelatedField()

    class Meta:
        model = Campaign
        exclude = ['id']

class JournalEntrySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    campaign = serializers.SlugRelatedField(slug_field='uuid',
                                            queryset=Campaign.objects.all())
    
    class Meta:
        model = JournalEntry
        exclude = ['id']

class PlayableCharacterSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = PlayableCharacter
        exclude = ['id']

class ItemSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    character = serializers.SlugRelatedField(slug_field='uuid',
                                            queryset=PlayableCharacter.objects.all())
    class Meta:
        model = Item
        exclude = ['id']         

class TalentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    character = serializers.SlugRelatedField(slug_field='uuid',
                                            queryset=PlayableCharacter.objects.all())
    class Meta:
        model = Talent
        exclude = ['id']         

class SpellSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    character = serializers.SlugRelatedField(slug_field='uuid',
                                            queryset=PlayableCharacter.objects.all())
    class Meta:
        model = Spell
        exclude = ['id']         