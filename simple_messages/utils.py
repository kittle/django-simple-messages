from datetime import datetime

from models import SimpleMessage


def add_message(user, message, level=30, expire=None, extra_tags=None):
    if not user.is_authenticated():
        return message
    m = SimpleMessage(user=user, message=message)
    m.save()


def get_messages(user):
    messages = SimpleMessage.objects.filter(user=user, read=False,
                        # TODO: expire_lt=datetime.now()
                        ).order_by('-created')
    messages.update(read=True)
    return messages
