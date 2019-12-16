from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=4000, null=True, blank=True)
    completed = models.BooleanField(default=False)
    audit_cd = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

