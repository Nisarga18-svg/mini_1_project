from django.db import models

from django.db import models

class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    question = models.TextField()
    answer = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
