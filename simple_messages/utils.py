from datetime import datetime

from django.db.models import F
from django.conf import settings

from models import SimpleMessage


def add_message(user, message, level=30, expire=None, extra_tags=None):
    if not user.is_authenticated():
        return message
    m = SimpleMessage(user=user, message=message)
    m.save()


def get_messages(user):
    messages = SimpleMessage.objects.filter(user=user, read=False,
                        n_seen__lt=getattr(settings, 'SIMPLE_MESSAGES_MAX_SEEN', 10),
                        # TODO: expire_lt=datetime.now()
                        ).order_by('-created')
    #import pudb; pudb.set_trace()
    #messages.update(read=True)
    messages.update(n_seen=F('n_seen') + 1)
    return messages
