from django.db import models

class Book(models.Model):
    cover = models.FileField(upload_to='images/', blank=True)
    name = models.CharField(max_length = 200)
    description = models.TextField()
    author = models.CharField(max_length = 100)

    def __str__(self):
        return "{},{},{},{}".format(self.cover, self.name, self.description, self.author)