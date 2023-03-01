import json
from .models import TempHumi, Gps
from django.views import View
from django.http import JsonResponse
from user.utils import login_decorator

#GPS , 온습도 값
class GpsTem(View):
    def get(self, request):
        try:
            tem = TempHumi.objects.get(id=1)
            gps = Gps.objects.get(id=1) 

            context = [{
                    "lat" : gps.lat,
                    "lng" : gps.lng,
                    "tem" : round(tem.temp, 2),
                    "humi": tem.humi
             }]
            return JsonResponse({'MESSAGE':context}, status=200)
        
        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR!"}, status=400)