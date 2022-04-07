import os

import pandas as pd
from django.core.files.uploadedfile import UploadedFile
from users.models import User
from wfrp.models import (AdvancedSkill, Armour, Campaign, Creature,
                         CreatureTrait, Item, PlayableCharacter, Spell, Talent,
                         Weapon)


def addDefaultCharacter(user: User,
                        campaign: Campaign,
                        character_name: str,
                        EXAMPLE_MEDIA_ROOT) -> bool:

    DEFAULT_CHARACTER_PATH = os.path.join(
        EXAMPLE_MEDIA_ROOT, 'default_characters.xlsx')
    ARMOUR_FILE_PATH = os.path.join(EXAMPLE_MEDIA_ROOT, 'default_armour.xlsx')
    ITEM_FILE_PATH = os.path.join(EXAMPLE_MEDIA_ROOT, 'default_items.xlsx')
    WEAPON_FILE_PATH = os.path.join(EXAMPLE_MEDIA_ROOT, 'default_weapons.xlsx')
    SPELL_FILE_PATH = os.path.join(EXAMPLE_MEDIA_ROOT, 'default_spells.xlsx')
    TALENT_FILE_PATH = os.path.join(EXAMPLE_MEDIA_ROOT, 'default_talents.xlsx')
    ADVANCEDSKILL_FILE_PATH = os.path.join(
        EXAMPLE_MEDIA_ROOT, 'default_advanced_skills.xlsx')
    DEFAULT_CHARACTERS = ['GUNNAR', 'MOLRELLA',
                          'FERDINAND', 'AMRIS', 'ELSE', 'BLANK']

    if character_name not in DEFAULT_CHARACTERS:
        return False
    else:
        # create default character
        char_data = pd.read_excel(DEFAULT_CHARACTER_PATH)
        char_data = char_data[char_data['character'] == character_name]
        char_data = pd.read_excel(DEFAULT_CHARACTER_PATH)
        avatar = str(char_data['avatar'][0])
        avatar_path = os.path.join(EXAMPLE_MEDIA_ROOT, avatar)
        full_pic = str(char_data['full_pic'][0])
        full_pic_path = os.path.join(EXAMPLE_MEDIA_ROOT, full_pic)
        char_data = char_data.drop(
            labels=['character', 'avatar', 'full_pic'], axis=1)
        char_data = char_data.to_dict('records')[0]
        character_instance = PlayableCharacter(user=user,
                                               campaign=campaign,
                                               **char_data)
        character_instance.save()
        character_instance.character_avatar.save(avatar, UploadedFile(
            file=open(avatar_path, 'rb'), content_type='image/png'))
        character_instance.character_picture.save(full_pic, UploadedFile(
            file=open(full_pic_path, 'rb'), content_type='image/png'))
        # Yep, I know these can be generalized into a single func:
        # create related items
        item_data = pd.read_excel(ITEM_FILE_PATH)
        item_data = item_data[item_data['character'] == character_name]
        item_data = item_data.drop(labels=['character'], axis=1)
        item_data = item_data.to_dict('records')
        for element in item_data:
            element.update({'user': user, 'character': character_instance})
        Item.objects.bulk_create([Item(**element) for element in item_data])
        # create related armour
        armor_data = pd.read_excel(ARMOUR_FILE_PATH)
        armor_data = armor_data[armor_data['character'] == character_name]
        armor_data = armor_data.drop(labels=['character'], axis=1)
        armor_data = armor_data.to_dict('records')
        for element in armor_data:
            element.update({'user': user, 'character': character_instance})
        Armour.objects.bulk_create([Armour(**element)
                                   for element in armor_data])
        # create related weapons
        weapon_data = pd.read_excel(WEAPON_FILE_PATH)
        weapon_data = weapon_data[weapon_data['character'] == character_name]
        weapon_data = weapon_data.drop(labels=['character'], axis=1)
        weapon_data = weapon_data.to_dict('records')
        for element in weapon_data:
            element.update({'user': user, 'character': character_instance})
        Weapon.objects.bulk_create([Weapon(**element)
                                   for element in weapon_data])
        # create related spells
        spell_data = pd.read_excel(SPELL_FILE_PATH)
        spell_data = spell_data[spell_data['character'] == character_name]
        spell_data = spell_data.drop(labels=['character'], axis=1)
        spell_data = spell_data.to_dict('records')
        for element in spell_data:
            element.update({'user': user, 'character': character_instance})
        Spell.objects.bulk_create([Spell(**element) for element in spell_data])
        # create related talents
        talent_data = pd.read_excel(TALENT_FILE_PATH)
        talent_data = talent_data[talent_data['character'] == character_name]
        talent_data = talent_data.drop(labels=['character'], axis=1)
        talent_data = talent_data.to_dict('records')
        for element in talent_data:
            element.update({'user': user, 'character': character_instance})
        Talent.objects.bulk_create([Talent(**element)
                                   for element in talent_data])
        # create related advanced skills
        advancedskill_data = pd.read_excel(ADVANCEDSKILL_FILE_PATH)
        advancedskill_data = advancedskill_data[advancedskill_data['character']
                                                == character_name]
        advancedskill_data = advancedskill_data.drop(
            labels=['character'], axis=1)
        advancedskill_data = advancedskill_data.to_dict('records')
        for element in advancedskill_data:
            element.update({'user': user, 'character': character_instance})
        AdvancedSkill.objects.bulk_create(
            [AdvancedSkill(**element) for element in advancedskill_data])


def addDefaultCampaign(campaign_master: User,
                       campaign_name: str,
                       campaign_description: str,
                       EXAMPLE_MEDIA_ROOT: str):
    if len(Campaign.objects.filter(name=campaign_name)) == 0:
        campaign = Campaign(master=campaign_master,
                            name=campaign_name,
                            description=campaign_description.strip())
        campaign.save()
        campaign.cover_image.save(f'ubersreik.jpg', UploadedFile(
            file=open(os.path.join(EXAMPLE_MEDIA_ROOT, 'ubersreik.jpg'), 'rb'), content_type='image/jpg'))
    else:
        campaign = Campaign.objects.get(name=campaign_name)
    return campaign


def addDefaultCreatures(EXAMPLE_MEDIA_ROOT: str):
    DEFAULT_CREATURE_PATH = os.path.join(
        EXAMPLE_MEDIA_ROOT, 'default_creatures.xlsx')
    creature_data = pd.read_excel(DEFAULT_CREATURE_PATH)
    creature_data = creature_data.to_dict('records')
    for item in creature_data:
        pic_path = os.path.join(EXAMPLE_MEDIA_ROOT, item['creature_picture'])
        # item['user'] = admin
        # item['campaign'] = campaign
        item['creature_picture'] = UploadedFile(file=open(pic_path, 'rb'),
                                                content_type='image/png')

    Creature.objects.bulk_create([Creature(**item) for item in creature_data])

    DEFAULT_CREATURETRAIT_PATH = os.path.join(
        EXAMPLE_MEDIA_ROOT, 'default_creature_traits.xlsx')
    creature_traits = pd.read_excel(DEFAULT_CREATURETRAIT_PATH)
    creature_traits = creature_traits.to_dict('records')
    for item in creature_traits:
        creature_name = item['creature_name']
        creature = Creature.objects.filter(name=creature_name)[0]
        _ = item.pop('creature_name', '')
        # item['user'] = admin
        # item['campaign'] = campaign
        trait = CreatureTrait(**item)
        trait.save()
        creature.traits.add(trait)
