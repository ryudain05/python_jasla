DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'askcompany',
        'USER': 'root',
        'PASSWORD': '2022jasla',
        'HOST': 'parkbomin.iptime.org',
        'PORT': '13306',
				'OPTIONS': {'charset': 'utf8mb4'}
    }
}

SECRET_KEY = '1ban7#uxmluwp-gl)9qmvnei=p%8b!k)(*^ld#d&1prm%!cyfq' #settings.py에 있는 secret_key 를 사용합니다.

ALGORITHM ='HS256'