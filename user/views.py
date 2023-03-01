import json, bcrypt, jwt, re

from django.views import View
from django.http import JsonResponse
from user.utils import login_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import User
from jasla.settings import SECRET_KEY

# 회원가입
class SignUp(View):
    def post(self, request):
        data = json.loads(request.body)
        print("--------------")
        print(data)
        try:
            p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$') #이메일 정규식 사용.

            if not p.match(data['email']): 
                return JsonResponse({'MESSAGE':'EMAIL_ERROR!'}, status=400)

            if len(data['password']) < 8:
                 return JsonResponse({'MESSAGE':'PASSWORD_IS_SHORT!'}, status=400)

            if User.objects.filter(email=data['email']).exists():                           
                return JsonResponse({'MESSAGE':'EMAIL_ALEADY_IN_USE'}, status=400)
            
            hash_password =  bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()) # encode로 바이트화
            hash_password = hash_password.decode('utf-8') # decode로 str 형태
        
            User.objects.create(
                name = data['name'],
                nickname = data['nickname'],
                email = data['email'],
                password = hash_password,
                phone = data['phone'],
            )
            return JsonResponse({'MESSAGE':'SUCCESS!'}, status=200)
        
        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR!"}, status=400)
 
 # 로그인 
class SignIn(View):
    def post(self, request):
        
        data = json.loads(request.body)
        try:
            user = User.objects.get(email=data['email'])
            
            if User.objects.filter(email=data['email']).exists(): # 이메일 존재
               
                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')): # 비밀번호 확인
                
                    secret       = SECRET_KEY
                    token        = jwt.encode({'user_id' : user.id}, secret, algorithm = 'HS256')   
                    
                    return JsonResponse({"access_token" : token, "user_nickname":user.nickname}, status=200)
                                  
                else: #비밀번호가 틀린 경우
                    
                    return JsonResponse({'MESSAGE':'INVALID_USER!'}, status=401)

            if not User.objects.filter(email=data['email']).exists():    # 이메일이 존재 하지 않는다.

                return JsonResponse({"MESSAGE": "INVALID_USER"}, status=401)
        
        
             
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=401)
        #except JSONDecodeError:
            #return JsonResponse({'MESSAGE': 'JSON_DECODE_ERROR'}, status=400)
        #except JSONDecodeError:
        

#테스트 api
class Test(View):
    def post(self, request):
        print("-----")
        print(request.body.decode('utf-8'))
        print("-----")
        #data = json.loads(request.body.decode('utf-8'))
        data = json.loads(request.body)
        try:
            #print("-------- body 값임-------")
            #print(data)
            #print("------------------")
            return JsonResponse({"MESSAGE" : "반가워요 소통해요"}, status=200)
        except json.decoder.JSONDecodeError:
            
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)

            
            
#닉네임 중복체크
class NameCheck(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            
            if User.objects.filter(nickname = data['nickname']).exists():

                return JsonResponse({'MESSAGE':'NICKNAME_ALEADY_IN_USE'}, status=409)

            else:
                
                return JsonResponse({'MESSAGE':'SUCCESS!'}, status=200)
        
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=401)

#내 정보         
class MyInfo(View):
    @login_decorator
    def get(self, request):

        try:
            user = request.user
            user = User.objects.get(email=user)
            

            context = [{
                "name"    : user.name,
                "email"  : user.email,
                "phone": user.phone,
                "nickname"  : user.nickname
            }]
            
            return JsonResponse({"MESSAGE" : context}, status=200)
        
        except KeyError:
            return JsonResponse({'MESSAGE':'INVALID_USER!'}, status=401)





