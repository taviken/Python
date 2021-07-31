from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here. (ie database models)
class Post(models.Model):
    """
    Class that represents a blog post, is the python interface to the database. Is part of the backend
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # the author is a 1 to many relation
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.title})'
