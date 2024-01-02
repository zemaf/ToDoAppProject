from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Tâche"

    def __str__(self):
        return self.title
