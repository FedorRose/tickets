from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic.base import RedirectView

from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('', RedirectView.as_view(url='tickets', permanent=False), name='index'),
    path('tickets/', tickets, name='tickets'),
    path('tickets/<int:pk>/', ticket, name='ticket'),
    path('backlog/<int:release>/', backlog, name='backlog'),
    path('my_page/', my_page, name='my_page'),
    path('team/', team, name='team'),
    path('new/', new, name='new'),
    path('dev_tickets/<int:pk>/', dev_tickets, name='dev_tickets'),
    path('closed_tickets/', closed_tickets, name='closed_tickets'),
    path('doc/', doc, name='doc'),
]
