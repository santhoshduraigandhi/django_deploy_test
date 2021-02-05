from django.db import models


# Create your models here.

class Jobs(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

# this function for View the Title name replace to Object
    def __str__(self):
        return self.title

