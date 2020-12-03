from django.views.generic import (
    TemplateView,
    ListView,
)

from rooms.models import Room


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class RoomListView(ListView):
    model = Room
    template_name = 'rooms.html'
    context_object_name = 'rooms'
