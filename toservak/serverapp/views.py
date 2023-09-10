import string
import random
from django.shortcuts import render
from . import models
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import renderer_classes
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer


@csrf_exempt
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def create_invite_code(request):
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    chat_id = request.POST.get('chat_id')

    chat_room = models.ChatRoom()
    chat_room.admin_id = chat_id
    chat_room.tasks_id = ''
    chat_room.users_id = ''
    models.ChatRoom.save(chat_room)

    invite_code = models.InviteCode()
    invite_code.code = code

    chat_room = models.ChatRoom.objects.latest('id').id
    invite_code.chat_room_id = chat_room
    models.InviteCode.save(invite_code)
    serializer = serializers.serialize('json', [invite_code])
    return HttpResponse(serializer, content_type='application/json')


@csrf_exempt
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def create_user(request):
    user = models.User()
    user.email = request.POST.get('email')
    user.name = request.POST.get('name')
    user.last_name = request.POST.get('lastname')
    user.chat_id = request.POST.get('chat_id')
    user.save()
    serializer = serializers.serialize('json', [user])
    return HttpResponse(serializer, content_type='application/json')

@csrf_exempt
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def create_task(request):
    task = models.Task1()
    task.name = request.POST.get('name')
    task.text = request.POST.get('text')
    task.if_done = False
    chat_room = models.ChatRoom.objects.filter(admin_id = request.POST.get('chat_id'))[0]
    id = chat_room.id
    task.chat_room_id = id
    task.save()
    serializer = serializers.serialize('json', [chat_room])
    return HttpResponse(serializer, content_type='application/json')


@csrf_exempt
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_actual_task(request, chat_id):
    chat_room = models.ChatRoom.objects.filter(admin_id = int(chat_id))
    chat = 0
    if len(chat_room) == 0:
        chat_room = models.ChatRoom.objects.all()
        for i in chat_room:
            if chat_id in i.users_id:
                chat = i.id
    else:
        chat = chat_room[0].id

    tasks = models.Task1.objects.filter(chat_room_id = chat, if_done = False)



    serializer = serializers.serialize('json', list(tasks))
    return HttpResponse(serializer, content_type='application/json')



@csrf_exempt
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_not_actual_task(request, chat_id):
    chat_room = models.ChatRoom.objects.filter(admin_id = int(chat_id))
    chat = 0
    if len(chat_room) == 0:
        chat_room = models.ChatRoom.objects.all()
        for i in chat_room:
            if chat_id in i.users_id:
                chat = i.id
    else:
        chat = chat_room[0].id

    tasks = models.Task1.objects.filter(chat_room_id = chat, if_done = True)



    serializer = serializers.serialize('json', list(tasks))
    return HttpResponse(serializer, content_type='application/json')


@csrf_exempt
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def set_not_actual(request):
    id = request.POST.get('id')
    print(id)
    print(models.Task1.objects.filter(id = int(id)))
    task = models.Task1.objects.filter(id = id)[0]
    task.if_done = True
    task.save()
    serializer = serializers.serialize('json', [task])
    return HttpResponse(serializer, content_type='application/json')













