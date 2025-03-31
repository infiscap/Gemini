# 베이스 이미지 설정 (Python 3.9 권장)
FROM python:3.9-slim-buster

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치 (requirements.txt 파일이 있다고 가정)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Streamlit 앱 소스 코드 복사
COPY . .

# Streamlit 앱 실행 명령 설정
CMD ["streamlit", "run", "app.py", "--browser.serverAddress=localhost", \
  "--server.enableCORS=false", \
  "--server.enableXsrfProtection=false", \
  "--server.port", "8080"] 

