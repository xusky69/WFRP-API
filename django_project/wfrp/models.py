from uuid import uuid4
from django.db import models

from django.conf import settings

# Create your models here.
class Campaign(models.Model):
  name = models.CharField(max_length=32)
  master = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='campaigns', on_delete=models.CASCADE)
  uuid = models.UUIDField(default=uuid4, editable=False)
  description = models.TextField(default="Enter a description for your campaign")
  creation_date = models.DateTimeField(auto_now_add=True)
  last_updated = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return f'{self.name}_{self.id}'

# class JournalEntry(models.Model):
#   name = models.CharField(max_length=32)
#   uuid = models.UUIDField(uuid4)
#   campaign = models.ForeignKey(Campaign, related_name='journal_entries', on_delete=models.CASCADE)
#   entry_text = models.TextField()
#   creation_date = models.DateTimeField(auto_now_add=True)
#   last_updated = models.DateTimeField(auto_now=True)

#   def __str__(self) -> str:
#     return f'{self.name}_{self.id}'