from django.db import models


class TimeStampedModel(models.Model):
    """[summary]
    An abstract class model that provides self-
    updating ``created`` and ``modified`` fields
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Note(TimeStampedModel):
    """[summary]
    Base model on which are web app based on
    """
    title = models.CharField(max_length=150)
    content = models.TextField()

    def __str__(self):
        return self.title
