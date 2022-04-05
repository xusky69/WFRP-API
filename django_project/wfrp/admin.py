from django.contrib import admin

from .models import (Campaign, Item, JournalEntry, PlayableCharacter, Spell,
                     Talent, Armour, Weapon, AdvancedSkill)

# Register your models here.
admin.site.register(Campaign)
admin.site.register(JournalEntry)
admin.site.register(PlayableCharacter)
admin.site.register(Talent)
admin.site.register(Item)
admin.site.register(Armour)
admin.site.register(Weapon)
admin.site.register(AdvancedSkill)