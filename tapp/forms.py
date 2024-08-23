from django import forms
from .models import Task

# Defining our forms
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date', 'avator', 'author', 'tag']