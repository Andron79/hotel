from django.urls import path

from pages.views import (
    IndexView,
    AboutView,
    RoomListView,
    ContactView,
)

app_name = 'pages'

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('rooms/', RoomListView.as_view(), name='rooms'),
    path('contact/', ContactView.as_view(), name='contact'),

]
