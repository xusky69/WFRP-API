from uuid import uuid4
from django.db import models
from django.conf import settings

from users.models import User

# Create your models here.
class Campaign(models.Model):
  name = models.CharField(max_length=32)
  master = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='campaigns', on_delete=models.CASCADE)
  uuid = models.UUIDField(default=uuid4, editable=False)
  description = models.TextField(default="Enter a description for your campaign")
  creation_date = models.DateTimeField(auto_now_add=True)
  last_updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = "Campaign"
    verbose_name_plural = "Campaigns"

  def __str__(self) -> str:
    return f'{self.name}_{self.id}'

class JournalEntry(models.Model):
  name = models.CharField(max_length=32)
  uuid = models.UUIDField(default=uuid4, editable=False)
  
  user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
  campaign = models.ForeignKey(Campaign, related_name='journal_entries', on_delete=models.CASCADE)
  
  entry_text = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  creation_date = models.DateTimeField(auto_now_add=True)
  last_updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = "journal entry"
    verbose_name_plural = "journal entries"

  def __str__(self) -> str:
    return f'{self.name}_{self.campaign}_{self.id}'