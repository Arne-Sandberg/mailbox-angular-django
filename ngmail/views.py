from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
import json
from ngmail.models import NGUser, NGMessage
from django.views.decorators.csrf import csrf_exempt
import time


# Create your views here.

def message_to_dict(msg):
    return {
        'id': msg.id,
        'sender': msg.sender.id,
        'recipient': msg.recipient.id,
        'text': msg.text,
        'sent': str(msg.date_and_time)
    }


def user_to_dict(usr):
    return {
        'id': usr.id,
        'firstName': usr.first_name,
        'lastName': usr.last_name,
        'gender': usr.gender,
        'address': usr.address,
        'email': usr.email,
        'avatarUrl': usr.avatar_url,
        'birthDate': str(usr.birthdate)
    }


def parse_id(item_id):
    if isinstance(item_id, int) and item_id > 0:
        return item_id
    elif isinstance(item_id, str):
        return parse_id(int(item_id)) if item_id and item_id.isdigit() else None
    else:
        return None


@csrf_exempt
def messages(request):
    me = NGUser.objects.get(first_name='Леонид')
    messages = [message_to_dict(m) for m in NGMessage.objects.filter(recipient=me).filter(sender__deleted=False).all()]
    return HttpResponse(
        json.dumps(messages),
        mimetype="application/json"
    )


@csrf_exempt
def users(request):
    users = [user_to_dict(u) for u in NGUser.objects.filter(deleted=False)]
    return HttpResponse(
        json.dumps(users),
        mimetype="application/json"
    )


@csrf_exempt
def edit_user(request, uid):
    user_id = parse_id(uid)
    if user_id is None:
        return HttpResponseBadRequest()
    user = NGUser.get_user_by_id(uid)
    if user is None:
        return HttpResponseBadRequest()
    user_data = request.POST.get('user', None)
    if user_data is None:
        return HttpResponseBadRequest()
    user_data = json.loads(user_data)
    # TODO: add server validation
    user.first_name = user_data['firstName']
    user.last_name = user_data['lastName']
    user.gender = user_data['gender']
    user.birhdate = time.strptime(user_data['birthDate'], '%Y-%m-%d')
    user.avatar_url = user_data['avatarUrl']
    user.email = user_data['email']
    user.address = user_data['address']
    user.save()
    return HttpResponse(
        json.dumps(user_to_dict(user)),
        mimetype="application/json"
    )


@csrf_exempt
def delete_contact(request, uid):
    user_id = parse_id(uid)
    if user_id is None:
        return HttpResponseBadRequest()
    user = NGUser.get_user_by_id(uid)
    if user is None:
        return HttpResponseBadRequest()
    user.deleted = True
    user.save()
    return HttpResponse(
        json.dumps(user_to_dict(user)),
        mimetype="application/json"
    )