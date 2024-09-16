from django.db import models


# Model for a todo list task category with a unique name
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

# Model for a simple todo list task with a title,
# description, due date, completed status and category
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title