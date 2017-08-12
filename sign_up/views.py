# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from custom_user_api.models import User
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse

# def create_account(request):
#   email = 

@csrf_exempt
def createUser(request):
    # userName = request.REQUEST.get('username', None)
    userPass = request.POST.get('password', None)
    userMail = request.POST.get('email', None)

    # TODO: check if already existed

    # **user = User.objects.create_user(userName, userMail, userPass)**
    # user.save()
    
    user = User.objects.create_user(email= userMail,
                                 password= userPass)

    return JsonResponse({'success' : 'OK' ,'user': user.email})

    # return render_to_response('home.html', context_instance=RequestContext(request))

