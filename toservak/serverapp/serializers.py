from rest_framework import serializers
from . import models


class User(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    chat_id = serializers.CharField(max_length=255)

    class Meta:
        model = models.User
        fields = '__all__'


class ChatRoom(serializers.ModelSerializer):
    admin_id = serializers.IntegerField()
    users_id = serializers.CharField
    tasks_id = serializers.CharField(max_length=255)

    class Meta:
        model = models.ChatRoom
        fields = '__all__'


class Task(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    text = serializers.CharField(max_length=255)
    chat_room_id = serializers.IntegerField()
    if_done = serializers.BooleanField


    class Meta:
        model = models.Task
        fields = '__all__'

class InviteCode(serializers.ModelSerializer):
    code = serializers.CharField(max_length=255)
    chat_room_id = serializers.IntegerField()

    class Meta:
        model = models.InviteCode
        fields = '__all__'