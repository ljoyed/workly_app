from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # This field is allowed to be empty/null for old users who never uploaded an image
    avatar_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"