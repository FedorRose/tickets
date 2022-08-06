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


class Ticket(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='author')
    developer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='developer')
    priority = models.CharField(max_length=10, choices=PRIORITIES, default='NORMAL')
    status = models.CharField(max_length=30, choices=STATUSES, default='NEW')
