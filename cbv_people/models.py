from django.db import models

class Person(models.Model):
    GENDER_TYPES = {
        "MAN": "Man",
        "WOMAN": "Woman"
    }
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER_TYPES, default=GENDER_TYPES["MAN"])

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"#{self.id} - {self.fullname}"

    class Meta:
        ordering = ["-birthday"]
        verbose_name = "Person"
        verbose_name_plural = "People"
