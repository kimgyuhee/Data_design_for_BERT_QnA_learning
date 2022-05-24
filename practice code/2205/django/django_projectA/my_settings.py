DATABASES = {
    'default':{
        # 1. 사용할 엔진 설정
        'ENGINE': 'django.db.backends.mysql',
        # 2. 연동할 MySQL의 데이터베이스 이름
        'NAME': 'projecta_db',
        # 3. DB 접속 계정명
        'USER': 'root',
        # 4. DB 패스워드
        'PASSWORD': 'test123',
        # 5. DB 주소
        'HOST': 'localhost',
        # 6. 포트번호
        'PORT': '3306',
    }
}

# 본인이 생성한 장고 프로젝트의 시크릿 키 복사해서 넣기
SECRET_KEY = 'django-insecure-6nu^k4%y+88=bbq&vfea3tzj!bm1e2!vj%om&v3=4hm!co2j!)'