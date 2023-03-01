import json
from user.models import User
from django.views import View
from django.http import JsonResponse
from user.utils import login_decorator

#어드민 유저정보 리스트
class UserList(View):
    @login_decorator
    def get(self, request):

        try:
            users = User.objects.exclude(is_super=1)

            context = [{
                "name"    : user.name,
                "email"  : user.email,
                "phone": user.phone,
                "nickname"  : user.nickname
            }for user in users]
            
            return JsonResponse({"MESSAGE" : context}, status=200)
        
        except KeyError:
            return JsonResponse({'MESSAGE':'INVALID_USER!'}, status=401)