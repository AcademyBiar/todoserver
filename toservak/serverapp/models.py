from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=255)


class ChatRoom(models.Model):
    admin_id = models.IntegerField()
    users_id = models.CharField
    tasks_id = models.CharField(max_length=255)


class Task1(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    chat_room_id = models.IntegerField()
    if_done = models.BooleanField(null=True)




class InviteCode(models.Model):
    code = models.CharField(max_length=255)
    chat_room_id = models.IntegerField()