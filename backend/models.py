from django.db import models
from django.contrib.auth.models import User


class Influencer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instagram_username = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.instagram_username)

class InstagramSession(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sessionid = models.CharField(max_length=255)  # Almacena el sessionid del usuario

    def __str__(self):
        return f"Session for {self.user.username}"