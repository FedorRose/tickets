from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .models import *


def my_page(request):
    if request.user.is_authenticated:
        tickets = Ticket.objects.filter(developer=request.user)
        username = request.user
        return render(request, 'main/home.html', context={'tickets': tickets, 'title': "Мои тикеты",
                                                          'username': username})
    else:
        return redirect('login')


def tickets(request):
    if request.user.is_authenticated:
        tickets = Ticket.objects.exclude(status='CLOSED')
        username = request.user
        return render(request, 'main/home.html', context={'tickets': tickets, 'title': "Все тикеты",
                                                          'username': username})
    else:
        return redirect('login')


def ticket(request, pk=None):
    if request.user.is_authenticated:
        ticket = Ticket.objects.get(pk=pk)
        username = request.user
        if request.method == 'POST':
            form = Status(request.POST)
            if form.is_valid():
                ticket.status = form.cleaned_data['choice_field']
                ticket.save()
                return redirect('ticket', ticket.id)
        else:
            form = Status()
        return render(request, 'main/home.html', context={'ticket': ticket, 'title': "Тикет #{}".format(pk),
                                                          'username': username, 'form': form})
    else:
        return redirect('login')


def team(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        username = request.user
        return render(request, 'main/team.html', context={'title': "Наша команда", 'users': users,
                                                          'username': username})
    else:
        return redirect('login')


def dev_tickets(request, pk=None):
    if request.user.is_authenticated:
        dev = User.objects.get(pk=pk)
        username = request.user
        tickets = Ticket.objects.filter(developer=dev)
        return render(request, 'main/home.html', context={'title': "Тикеты ", 'tickets': tickets, 'username': username})
    else:
        return redirect('login')


def new(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            if form.is_valid():
                new_ticket = form.save(commit=False)
                new_ticket.author = request.user
                new_ticket.status = 'NEW'
                new_ticket.save()
                return redirect('tickets')
        else:
            form = AddPostForm()
        username = request.user
        return render(request, 'main/new.html', context={'form': form, 'title': "Новый тикет", 'username': username})

    else:
        return redirect('login')


def closed_tickets(request):
    if request.user.is_authenticated:
        tickets = Ticket.objects.filter(status='CLOSED')
        return render(request, 'main/home.html', context={'tickets': tickets, 'title': "Закрытые тикеты"})
    else:
        return redirect('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    success_url = reverse_lazy('my_page')
    template_name = 'registration/login.html'
