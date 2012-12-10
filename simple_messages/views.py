from django.views.generic import  ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from utils import get_messages
#from models import Message


class MessagesView(ListView):
    template_name = 'simple_messages/simple_messages_list.html'
    paginate_by = 50

    def get_queryset(self):
        return get_messages(self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MessagesView, self).dispatch(*args, **kwargs)
