from django.db import models
from apps.authentication.models import User


class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams')
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leader_teams')
    image = models.ImageField(upload_to='teams/')
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']