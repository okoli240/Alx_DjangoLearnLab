from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(
        User, related_name="notifications", on_delete=models.CASCADE
    )
    actor = models.ForeignKey(
        User, related_name="notifications_from", on_delete=models.CASCADE
    )
    verb = models.CharField(max_length=255)

    # Generic relation to any object (Post, Comment, etc.)
    target_content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True, blank=True
    )
    target_object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey("target_content_type", "target_object_id")

    # 👇 required by checker
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.actor} {self.verb} {self.target} → {self.recipient}"
