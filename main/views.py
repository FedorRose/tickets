from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import *
from .models import *

# OPEN_STATUSES = ('NEW', 'ASSIGNED-DEV', 'REVIEW-NEEDED', 'RESOLVED-DEV', )


def my_page(request):
    tickets = Ticket.objects.filter(developer=request.user).exclude(status='CLOSED')
    username = request.user
    return render(request, 'main/home.html', context={'tickets': tickets, 'title': "Мои тикеты", 'username': username})


def tickets(request):
    tickets = Ticket.objects.exclude(status='CLOSED')
    username = request.user
    return render(request, 'main/home.html', context={'tickets': tickets, 'title': "Все тикеты", 'username': username})


def ticket(request, pk=None):
    curr_ticket = Ticket.objects.get(pk=pk)
    notes = Comment.objects.filter(ticket=curr_ticket)
    username = request.user

    if request.method == 'POST':  # обработка форм
        if request.POST.get("form_type") == 'form_status':  # форма статуса и трудозатрат
            form_status = Status(request.POST)
            if form_status.is_valid():
                curr_ticket.status = form_status.cleaned_data['choice_field']
                if form_status.cleaned_data['time']:
                    curr_ticket.time = curr_ticket.time + int(form_status.cleaned_data['time'])
                curr_ticket.save()
                return redirect('ticket', curr_ticket.id)
        elif request.POST.get("form_type") == 'form_notes':  # форма комментариев
            form = CommentForm(request.POST)
            if form.is_valid():
                note = form.save(commit=False)
                note.dev = request.user
                note.ticket = curr_ticket
                note.save()
                return redirect('ticket', curr_ticket.id)

    form_status = Status({'choice_field': curr_ticket.status})
    form = CommentForm()

    return render(request, 'main/home.html', context={'ticket': curr_ticket, 'title': "Тикет #{}".format(pk),
                                                      'username': username, 'form_status': form_status,
                                                      'form_notes': form, 'notes': notes})


def team(request):
    users = User.objects.all()
    username = request.user
    return render(request, 'main/team.html', context={'title': "Наша команда", 'users': users,
                                                      'username': username})


def dev_tickets(request, pk=None):
    dev = User.objects.get(pk=pk)
    username = request.user
    tickets = Ticket.objects.filter(developer=dev).exclude(status='CLOSED')
    return render(request, 'main/home.html', context={'title': "Тикеты ", 'tickets': tickets, 'username': username})


def new(request):
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


def closed_tickets(request):
    tickets = Ticket.objects.filter(status='CLOSED')
    return render(request, 'main/home.html', context={'tickets': tickets, 'title': "Закрытые тикеты"})


def doc(request):
    return render(request, 'main/doc.html', context={'title': "Документация"})


class LoginUser(LoginView):
    form_class = LoginUserForm
    success_url = reverse_lazy('my_page')
    template_name = 'registration/login.html'
