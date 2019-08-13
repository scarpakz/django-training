from django.db import models

class Book(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    author = models.CharField(max_length = 100)

    def __str__(self):
        return "{},{},{}".format(self.name, self.description, self.author)