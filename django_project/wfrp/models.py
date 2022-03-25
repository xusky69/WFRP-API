from uuid import uuid4
from django.db import models
from django.conf import settings

from users.models import User

class Campaign(models.Model):
  name = models.CharField(max_length=32, blank=True, default='')
  master = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='campaigns', on_delete=models.CASCADE)
  uuid = models.UUIDField(default=uuid4, editable=False)
  description = models.TextField(default="Enter a description for your campaign")
  creation_date = models.DateTimeField(auto_now_add=True)
  last_updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = "Campaign"
    verbose_name_plural = "Campaigns"

  def __str__(self) -> str:
    return f'{self.name}_{self.uuid}'

class JournalEntry(models.Model):
  name = models.CharField(max_length=32, blank=True, default='')
  uuid = models.UUIDField(default=uuid4, editable=False)
  
  user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
  campaign = models.ForeignKey(Campaign, related_name='journal_entries', on_delete=models.CASCADE)
  
  entry_text = models.TextField(blank=True, default='')
  date = models.DateTimeField(auto_now_add=True)
  creation_date = models.DateTimeField(auto_now_add=True)
  last_updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = "journal entry"
    verbose_name_plural = "journal entries"

  def __str__(self) -> str:
    return f'{self.name}_{self.campaign}_{self.uuid}'

class PlayableCharacter(models.Model):
  uuid = models.UUIDField(default=uuid4, editable=False)
  user = models.ForeignKey(User, related_name='character', on_delete=models.CASCADE)
  creation_date = models.DateTimeField(auto_now_add=True)
  last_updated = models.DateTimeField(auto_now=True)
  
  ### general stuff
  name = models.CharField(max_length=32)
  species = models.CharField(max_length=32, blank=True, default='')
  career = models.CharField(max_length=32, blank=True, default='')
  career_level = models.CharField(max_length=32, blank=True, default='')
  career_path = models.CharField(max_length=32, blank=True, default='')
  status = models.CharField(max_length=32, blank=True, default='')
  age = models.CharField(max_length=32, blank=True, default='')
  height = models.CharField(max_length=32, blank=True, default='')
  hair = models.CharField(max_length=32, blank=True, default='')
  eyes = models.CharField(max_length=32, blank=True, default='')
  skin_color = models.CharField(max_length=32, blank=True, default='')
  mother = models.CharField(max_length=32, blank=True, default='')
  father = models.CharField(max_length=32, blank=True, default='')
  siblings = models.CharField(max_length=32, blank=True, default='')
  couple = models.CharField(max_length=32, blank=True, default='')
  birthplace = models.CharField(max_length=32, blank=True, default='')

  ### character details
  background_story = models.TextField(blank=True, default='')
  motivation = models.TextField(blank=True, default='')
  personal_relations = models.TextField(blank=True, default='')
  secrets = models.TextField(blank=True, default='')
  notes = models.TextField(blank=True, default='')

  ### characteristics
  weapon_skill = models.IntegerField(default=0)
  ballistic_skill = models.IntegerField(default=0)
  strength = models.IntegerField(default=0)
  toughness = models.IntegerField(default=0)
  initiative = models.IntegerField(default=0)
  agility = models.IntegerField(default=0)
  dexterity = models.IntegerField(default=0)
  intelligence = models.IntegerField(default=0)
  willpower = models.IntegerField(default=0)
  fellowship = models.IntegerField(default=0)

  ### fate
  fate = models.IntegerField(default=0)
  fortune = models.IntegerField(default=0)

  ### resilience
  resilience = models.IntegerField(default=0)
  resolve = models.IntegerField(default=0)
  motivation = models.IntegerField(default=0)

  ### experience
  current = models.IntegerField(default=0)
  spent = models.IntegerField(default=0)

  ### movement
  movement = models.IntegerField(default=0)
  walk = models.IntegerField(default=0)
  run = models.IntegerField(default=0)

  ### basic skills
  art = models.IntegerField(default=0)
  athletics = models.IntegerField(default=0)
  bribery = models.IntegerField(default=0)
  charm = models.IntegerField(default=0)
  charm_animal = models.IntegerField(default=0)
  climb = models.IntegerField(default=0)
  cool = models.IntegerField(default=0)
  consume_alcohol = models.IntegerField(default=0)
  dodge = models.IntegerField(default=0)
  drive = models.IntegerField(default=0)
  endurance = models.IntegerField(default=0)
  entertain = models.IntegerField(default=0)
  gamble = models.IntegerField(default=0)

  ### basic skills
  gossip = models.IntegerField(default=0)
  haggle = models.IntegerField(default=0)
  intimidate = models.IntegerField(default=0)
  intuition = models.IntegerField(default=0)
  leadership = models.IntegerField(default=0)
  melee_basic = models.IntegerField(default=0)
  navigation = models.IntegerField(default=0)
  outdoor_survival = models.IntegerField(default=0)
  perception = models.IntegerField(default=0)
  ride = models.IntegerField(default=0)
  row = models.IntegerField(default=0)
  stealth = models.IntegerField(default=0)

  ### grouped & advanced skills
  ### wip (is this needed tho?)

  ### talents are a one-to-many relation to Talents
  short_term_ambitions = models.TextField(blank=True, default='')
  long_term_ambitions = models.TextField(blank=True, default='')

  ### armour
  ### wip

  ### psychology
  psychology = models.TextField(blank=True, default='')

  ### corruption
  corruption = models.IntegerField(default=0)
  mutations = models.TextField(blank=True, default='')

  ### wealth
  wealth = models.IntegerField(default=0)

  ### wounds
  wounds = models.IntegerField(default=0)

  ### armour points
  right_arm = models.IntegerField(default=0)
  left_arm = models.IntegerField(default=0)
  head = models.IntegerField(default=0)
  right_leg = models.IntegerField(default=0)
  left_leg = models.IntegerField(default=0)
  body = models.IntegerField(default=0)

  ### trappings
  ### wip (is this needed tho?)  

  class Meta:
    verbose_name = 'playable character'
    verbose_name_plural = 'playable characters'

  def __str__(self) -> str:
    return f'{self.name}_{self.uuid}'

class Spell(models.Model):
  name = models.CharField(max_length=32, blank=True, default='')
  uuid = models.UUIDField(default=uuid4, editable=False)
  user = models.ForeignKey(User, related_name='spell', on_delete=models.CASCADE)
  creation_date = models.DateTimeField(auto_now_add=True)
  last_updated = models.DateTimeField(auto_now=True)
  character = models.ForeignKey(PlayableCharacter, related_name='spell', on_delete=models.CASCADE)
  description = models.TextField(blank=True, default='')
  # effect = models.TextField(blank=True, default='')

  class Meta:
    verbose_name = 'spell'
    verbose_name_plural = 'spells'

class Talent(models.Model):
  name = models.CharField(max_length=32, blank=True, default='')
  uuid = models.UUIDField(default=uuid4, editable=False)
  user = models.ForeignKey(User, related_name='talent', on_delete=models.CASCADE)
  creation_date = models.DateTimeField(auto_now_add=True)
  last_updated = models.DateTimeField(auto_now=True)
  character = models.ForeignKey(PlayableCharacter, related_name='talent', on_delete=models.CASCADE)
  description = models.TextField(blank=True, default='')
  # effect = models.TextField(blank=True, default='')

  class Meta:
    verbose_name = 'talent'
    verbose_name_plural = 'talents'

class Item(models.Model):
  ITEM_CHOICES = [('weapon', 'weapon'), 
                  ('armor', 'armor'), 
                  ('consumable', 'consumable'), 
                  ('jewel', 'jewel'),
                  ('trinket', 'trinket'),
                  ('other', 'other')]
  
  name = models.CharField(max_length=32, blank=True, default='')
  uuid = models.UUIDField(default=uuid4, editable=False)
  user = models.ForeignKey(User, related_name='item', on_delete=models.CASCADE)
  creation_date = models.DateTimeField(auto_now_add=True)
  last_updated = models.DateTimeField(auto_now=True)
  character = models.ForeignKey(PlayableCharacter, related_name='item', on_delete=models.CASCADE)
  description = models.TextField(blank=True, default='')  
  item_type = models.CharField(max_length=32, choices=ITEM_CHOICES)
  # effect = models.TextField(blank=True, default='')

  class Meta:
    verbose_name = 'item'
    verbose_name_plural = 'items'

  def __str__(self) -> str:
    return f'{self.name}_{self.character}_{self.uuid}'