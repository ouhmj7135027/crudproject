from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 20) 
    body = models.TextField()
    date = models.DateTimeField('date published')

    def sum(self):
        return self.body[:2]
