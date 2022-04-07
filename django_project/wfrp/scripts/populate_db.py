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

    users = [{'name': 'ricardo'},
             {'name': 'danna'},
             {'name': 'omar'},
             {'name': 'caceres'},
             {'name': 'aleja'},
             {'name': 'elliot'},
             {'name': 'felipe'},
             {'name': 'velez'}]

    for user in users:
        user_instance = User.objects.create_user(username=user['name'],
                                                 password=f'{user["name"]}_changeme')
        user_instance.save()

    admin = User.objects.create_user('admin', password='123')
    admin.is_superuser = True
    admin.is_staff = True
    admin.save()

    campaign_master = User.objects.get(username='velez')
    campaign_name = 'Haciendo la ronda'
    campaign_description = '''
    Los Personajes, que paseaban por el mercado de Ubersreik, se ven metidos en un tumulto y, más tarde, se les acusa de instigarlo. Misteriosamente, una abogada local interviene y convence al juez responsable del caso de que permita a los Personajes que paguen su ‘deuda’ trabajando como miembros de la Guardia.

    Pronto, el grupo se ve patrullando las calles de Ubersreik con Rudi Klumpenklug, un sargento de la guardia absolutamente corrupto. Los guardias temporales se ven expuestos a diversos delitos, ninguno de los cuales Klumpenklug muestra interés alguno por perseguir, dejando que los Personajes resuelvan, ignoren o incluso exploten cada situación como prefieran.

    Por último, Ilse Fassenwütend se pone en contacto con el grupo. Fassenwütend es una guarda de caminos, que afirma ser capaz de hacer que la sentencia de los Personajes sea conmutada si le ayudan a escoltar a un criminal al lugar donde debe ser ejecutado.

    Sin embargo, no será tarea fácil. El grupo tendrá ante sí una noche horrorosa, llevando a un hombre aterrorizado a través de unas calles extrañamente alteradas mientras Morrslieb, la luna del Caos, está en cuarto creciente (y por lo tanto brilla en el cielo) y sectarios mutantes los atacan por todos lados ¿Conseguirán los Personajes proteger al hombre, que afirma ser inocente, para luego llevarlo hasta el cadalso? ¿O elegirán un camino distinto?
    '''

    campaign = addDefaultCampaign(campaign_master,
                                  campaign_name,
                                  campaign_description,
                                  EXAMPLE_MEDIA_ROOT)

    user = User.objects.filter(username='ricardo')[0]
    campaign = Campaign.objects.all()[0]
    addDefaultCharacter(user=user, campaign=campaign,
                        character_name='GUNNAR', EXAMPLE_MEDIA_ROOT=EXAMPLE_MEDIA_ROOT)
    character_instance = PlayableCharacter.objects.filter(
        name='Gunnar Hrolfsson')[0]

    addDefaultCreatures(EXAMPLE_MEDIA_ROOT)
