from django.db import models

# Create your models here.

class FetchReport(models.Model):
    fetch_report = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)