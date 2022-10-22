from django.contrib.auth.models import User
from django.db import models

PRIORITIES = (
    ('NORMAL', 'NORMAL'),
    ('LOW', 'LOW'),
    ('HIGH', 'HIGH'),
)

STATUSES = (
    ('NEW', 'NEW'),
    ('ASSIGNED-DEV', 'ASSIGNED-DEV'),
    ('REVIEW-NEEDED', 'REVIEW-NEEDED'),
    ('RESOLVED-DEV', 'RESOLVED-DEV'),
    ('CLOSED', 'CLOSED'),
)

CATS = (
    ('BACKEND', 'BACKEND'),
    ('ANDROID', 'ANDROID'),
)


class Ticket(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='author')
    developer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='developer')
    priority = models.CharField(max_length=10, choices=PRIORITIES, default='NORMAL')
    status = models.CharField(max_length=30, choices=STATUSES, default='NEW')
    time = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=100, choices=CATS, null=True)


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    dev = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='dev')
    ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True, related_name='ticket')
