from django.db import models


class Todo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=20)
    completed = models.BooleanField(default=False)


