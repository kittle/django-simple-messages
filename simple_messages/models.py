#import os.path
#from urlparse import urlparse

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
#from django.utils.translation import ugettext as _
#from django.utils.http import urlquote
#from django.contrib.localflavor.us.models import PhoneNumberField

#from userena.models import UserenaBaseProfile

#from django.contrib.messages.storage.base import Message

from django.contrib.messages.storage.base import Message


class SimpleMessage(models.Model):
    user = models.ForeignKey(User)
    message = models.TextField()
    level = models.IntegerField(default=30)
    extra_tags = models.CharField(max_length=128, null=True, blank=True)
    read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    expires = models.DateTimeField(null=True, blank=True)

    def as_message(self):
        return Message(self.level, self.message, extra_tags=None)
