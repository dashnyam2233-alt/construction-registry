@echo off
cd /d "D:\Барилгын салбарын бүртгэл\construction_registry_mvp"
call .venv\Scripts\activate
python auto_tender.py >> tender_log.txt 2>&1