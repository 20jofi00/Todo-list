from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="tasks", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("is_completed", "-created_at")
