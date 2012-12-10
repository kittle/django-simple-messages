from django.contrib.messages.storage.base import BaseStorage

from utils import add_message, get_messages
from models import SimpleMessage


class ModelStorage(BaseStorage):
    """
    Stores messages in the model
    """
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

    def update(self, response):
        self._prepare_messages(self._queued_messages)
        return self._store(self._queued_messages, response)
