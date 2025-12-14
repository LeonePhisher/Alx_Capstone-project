from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):  #Todo table
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.CharField(max_length=100)
    is_completed=models.BooleanField(default=False)
    Timestamp=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.content