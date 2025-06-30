from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=(('draft', 'Draft'), ('published', 'Published')), default='draft', max_length=10)

    def __str__(self):
        return self.title
