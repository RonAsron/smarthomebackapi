# Dockerfile for Django Backend
FROM python:3.9-slim

# กำหนด working directory
WORKDIR /app

# คัดลอกไฟล์ทั้งหมดจากโฟลเดอร์ปัจจุบัน (ที่อยู่ในเครื่อง) ไปยัง /app ภายในคอนเทนเนอร์
COPY . /app/

# ติดตั้ง dependencies
RUN pip install --no-cache-dir -r requirements.txt

# รัน Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
