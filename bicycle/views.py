import json
from .models import Bicycle
from user.models import User
from django.views import View
from django.http import JsonResponse
from user.utils import login_decorator


class BicycleUp(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        
        try:

            user     = request.user
            
            Bicycle.objects.create(
                nickname = data['nickname'],
                modelname = data['modelname'],
                year = data['year'],
                type = data['type'],
                user = user
            )

            return JsonResponse({'MESSAGE':'SUCCESS!'}, status=200)
           
        except KeyError:
            return JsonResponse({'MESSAGE':'INVALID_USER!'}, status=401)
