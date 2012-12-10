from django.contrib.messages.storage.base import BaseStorage

from utils import add_message, get_messages
from models import SimpleMessage


class ModelStorage(BaseStorage):
    """
    Stores messages in the model
    """
    #session_key = '_messages'
    '''
    def __init__(self, request, *args, **kwargs):
        assert hasattr(request, 'session'), "The session-based temporary "\
            "message storage requires session middleware to be installed, "\
            "and come before the message middleware in the "\
            "MIDDLEWARE_CLASSES list."
        super(ModelStorage, self).__init__(request, *args, **kwargs)
    '''
    def _get(self, *args, **kwargs):
        if not self.request.user.is_authenticated():
            return [], False
        return (map(lambda m: m.as_message(), get_messages(self.request.user)),
                True)

    def _store(self, messages, response, *args, **kwargs):
        """
        Stores a list of messages.
        """
        if not self.request.user.is_authenticated():
            return []
        for message in messages:
            add_message(self.request.user, message.message, level=message.level)
        return []
