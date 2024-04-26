# Python 이미지를 기반으로 설정
FROM python:3.8

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements/requirements.txt /app/
RUN pip install -r requirements.txt

# 애플리케이션 코드 복사
COPY . /app/

# Gunicorn으로 애플리케이션 실행 (포트는 나중에 명령어로 지정)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "testProject.wsgi:application"]