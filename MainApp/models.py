from django.db import models

# Create your models here.

class Topic(models.Model): #we are inheriting everything from the models class
    text = models.CharField(max_length=200) #this text field is the name of the topic 
    date_added = models.DateTimeField(auto_now_add=True) 

    def __str__(self): #this string method returns whatever you want it to return 
        return self.text #if you do print topic if you would give you the name of the topic 



class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)#allows us to link these two and entry is foreign key to topic
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}..." #returning the text field and only returning the first 50 characters of that field