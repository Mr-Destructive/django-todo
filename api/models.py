from django.db import models
from django.contrib.auth.models import User

options = (
('done', 'Done'),
('pending', 'Pending'),
)

class Todo(models.Model):

    task = models.CharField(max_length=255)
    status = models.CharField(max_length=16, choices=options, default='pending')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")

    def __str__(self):
        return self.task


