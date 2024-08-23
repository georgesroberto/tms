from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}" 


class Tag(models.Model):
    name = models.CharField(max_length=26)

    def __str__(self):
        return f"{self.name}" 
    
    
class Task(models.Model):
    status_choices = {
        'due': 'Pending',
        'done': 'Completed'
    }
    
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=status_choices, default='due')
    created_at = models.DateField(auto_now=True)
    due_date = models.DateField()
    avator = models.ImageField(upload_to='profiles/', default='a.png')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, related_name='tasks')


    def __str__(self):
        return f"{self.title} {self.description} {self.status}"
    

    def get_tag_name(self):
        return 'Accessed'


from tapp.signals import (test_pre_signal, test_post_signal)