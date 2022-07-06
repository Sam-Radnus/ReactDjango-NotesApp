from django.db import models

# Create your models here.
#databse replica

#python classes inherit from django

class Note(models.Model):
    body=models.TextField(null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)#saves the time whenever we update it
    created=models.DateTimeField(auto_now_add=True)#saves the time whenever we create it

    def __str__(self):
        return self.body[0:50]