from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    homepage = models.URLField('Website', blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gamer_tag = models.CharField(max_length=200, blank=True)
    forum_sig = models.CharField(max_length=200, blank=True)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)

    def __unicode__(self):
        return 'Profile of user: {}'.format(self.user.username)