from rest_framework import serializers
from wfrp.models import (AdvancedSkill, Armour, Campaign, Creature,
                         CreatureTrait, Item, JournalEntry, Memory,
                         PlayableCharacter, Spell, Talent, Weapon)


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
    campaign = serializers.SlugRelatedField(slug_field='uuid',
                                            queryset=Campaign.objects.all())

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


class ArmourSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    character = serializers.SlugRelatedField(slug_field='uuid',
                                             queryset=PlayableCharacter.objects.all())

    class Meta:
        model = Armour
        exclude = ['id']


class WeaponSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    character = serializers.SlugRelatedField(slug_field='uuid',
                                             queryset=PlayableCharacter.objects.all())

    class Meta:
        model = Weapon
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


class AdvancedSkillSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    character = serializers.SlugRelatedField(slug_field='uuid',
                                             queryset=PlayableCharacter.objects.all())

    class Meta:
        model = AdvancedSkill
        exclude = ['id']


class MemorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    campaign = serializers.SlugRelatedField(slug_field='uuid',
                                            queryset=Campaign.objects.all())

    class Meta:
        model = Memory
        exclude = ['id']


class CreatureSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    campaign = serializers.SlugRelatedField(slug_field='uuid',
                                            queryset=Campaign.objects.all())
    traits = serializers.SerializerMethodField()

    class Meta:
        model = Creature
        exclude = ['id', 'is_default']

    def get_traits(self, inst):
        traits = inst.traits.all()
        traits = [item.uuid for item in traits]
        return traits


class CreatureTraitSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    campaign = serializers.SlugRelatedField(slug_field='uuid',
                                            queryset=Campaign.objects.all())

    class Meta:
        model = CreatureTrait
        exclude = ['id', 'is_default']
