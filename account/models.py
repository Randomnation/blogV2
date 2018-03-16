from django.db import models
from django.contrib.auth.models import User
import uuid


class EmailVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    verification_code = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.user.username

    class Meta:
        permissions = (
            ("verified", "User has verified their email address."),

        )