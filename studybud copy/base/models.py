from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length= 200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User,on_delete= models.SET_NULL, null = True)
    topic = models.ForeignKey(Topic,on_delete= models.SET_NULL, null = True)
    name = models.CharField(max_length=200)
    description = models.TextField(null = True,blank=True)
    participants = models.ManyToManyField(User,related_name= 'participants',blank =True)
    updated = models.DateTimeField(auto_now= True)
    created = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self) :
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    # Specify when the parent class is deleted the cascade will delete every message associates with that model
    room = models.ForeignKey(Room,on_delete= models.CASCADE)
    # textfield takes nothing because we want the user to input a message
    body = models.TextField()
    # records date everytime  an update is made to the messade
    updated = models.DateTimeField(auto_now= True)
    # records the date and time it was first created
    created = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.body[:50]
