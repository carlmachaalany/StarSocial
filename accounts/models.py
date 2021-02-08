from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        # username fields comes built in with auth.models.User
        return "@{}".format(user.username)
