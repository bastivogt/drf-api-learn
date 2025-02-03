from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.fullname}"




class Book(models.Model):
    title = models.CharField(max_length=255)
    #author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    authors = models.ManyToManyField(Author, blank=True, related_name="books")

    def __str__(self):
        return f"{self.title}"
