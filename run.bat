@echo off
cd /d C:\Users\dell\Desktop\construction_registry_mvp
call .venv\Scripts\activate
python manage.py runserver 127.0.0.1:8000
pause
