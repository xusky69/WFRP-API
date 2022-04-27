import os

import django
from users.models import User
from wfrp.models import (AdvancedSkill, Armour, Campaign, Creature,
                         CreatureTrait, Item, PlayableCharacter, Spell, Talent,
                         Weapon)
from wfrp.scripts.default_content import (addDefaultCampaign,
                                          addDefaultCharacter,
                                          addDefaultCreatures)

# os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
# django.setup()


def run():

    EXAMPLE_MEDIA_ROOT = 'wfrp/example_media/'

    Campaign.objects.all().delete()
    PlayableCharacter.objects.all().delete()
    Item.objects.all().delete()
    Armour.objects.all().delete()
    Talent.objects.all().delete()
    Spell.objects.all().delete()
    AdvancedSkill.objects.all().delete()
    Weapon.objects.all().delete()
    User.objects.all().delete()
    Creature.objects.all().delete()
    CreatureTrait.objects.all().delete()

    ### Why? calling the delete() method in bulk does not always call the overriden method
    ### hence, doesn't delete the remote S3 images
    # [item.delete() for item in Campaign.objects.all()]
    # [item.delete() for item in PlayableCharacter.objects.all()]
    # [item.delete() for item in Item.objects.all()]
    # [item.delete() for item in Armour.objects.all()]
    # [item.delete() for item in Talent.objects.all()]
    # [item.delete() for item in Spell.objects.all()]
    # [item.delete() for item in AdvancedSkill.objects.all()]
    # [item.delete() for item in Weapon.objects.all()]
    # [item.delete() for item in User.objects.all()]
    # [item.delete() for item in Creature.objects.all()]
    # [item.delete() for item in CreatureTrait.objects.all()]

    users = [
        {'name': 'gunnar', 'character': 'GUNNAR'},
        {'name': 'else', 'character': 'ELSE'},
        {'name': 'amris', 'character': 'AMRIS'},
        {'name': 'ferdinand', 'character': 'FERDINAND'},
        {'name': 'molrella', 'character': 'MOLRELLA'},
        {'name': 'master', 'character': ''}
    ]

    for user in users:
        user_instance = User.objects.create_user(username=user['name'],
                                                 password=f'{user["name"]}123')
        user_instance.save()

    admin = User.objects.create_user('admin', password='123')
    admin.is_superuser = True
    admin.is_staff = True
    admin.save()

    campaign_master = User.objects.get(username='master')
    campaign_name = 'Doing the rounds'
    campaign_description = '''
The Characters, strolling through the Ubersreik marketplace, are caught up in a riot and later charged with instigating it. Mysteriously, a local lawyer intervenes and convinces the judge in charge of the case to allow the Characters to pay their 'debt' by working as members of the Guard.

Soon, the group finds themselves patrolling the streets of Ubersreik with Rudi Klumpenklug, a thoroughly corrupt sergeant of the Guard. The temporary guards are exposed to various crimes, none of which Klumpenklug shows any interest in pursuing, leaving the Characters to resolve, ignore or even exploit each situation as they prefer.

Finally, Ilse Fassenwütend contacts the group. Fassenwütend is a road guard, who claims to be able to have the Characters' sentences commuted if they help her escort a criminal to the place where he is to be executed.

However, it will not be an easy task. The group will have a horrific night ahead of them, leading a terrified man through strangely altered streets while Morrslieb, the Chaos moon, is in the crescent (and therefore shining in the sky) and mutant cultists attack them from all sides. Will the Characters manage to protect the man, who claims to be innocent, and then take him to the scaffold? Or will they choose a different path?
'''

    campaign = addDefaultCampaign(campaign_master,
                                  campaign_name,
                                  campaign_description,
                                  EXAMPLE_MEDIA_ROOT)

    for user_entry in users:
        if len(user_entry['character']) > 0:
            user = User.objects.filter(username=user_entry['name'])[0]
            campaign = Campaign.objects.all()[0]
            addDefaultCharacter(user=user,
                                campaign=campaign,
                                character_name=user_entry['character'],
                                EXAMPLE_MEDIA_ROOT=EXAMPLE_MEDIA_ROOT)

    addDefaultCreatures(EXAMPLE_MEDIA_ROOT)
