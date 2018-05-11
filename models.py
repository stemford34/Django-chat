from django.db import models

from registration.models import UserInfo


class DialogInfo(models.Model):
    dialog_id = models.CharField(max_length=61)
    creator_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=61)


class DialogMassage(models.Model):
    dialog_id = models.ForeignKey(DialogInfo, on_delete=models.CASCADE)
    sender_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    text = models.TextField()
    time_create = models.DateTimeField('date send')


class DialogUsers(models.Model):
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    dialog_id = models.ForeignKey(DialogInfo, on_delete=models.CASCADE)
    joined = models.DateTimeField('date create')
    last_change = models.DateTimeField('last send')
