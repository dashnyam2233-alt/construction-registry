import os

views_path = r"apps\registry\views.py"

with open(views_path, "r", encoding="utf-8") as f:
    content = f.read()

# Хуучин json.loads дараах хэсгийг олж орлуулна
old_part = '''            try:
                result = json.loads(raw)
            except Exception as je:
                result = {"error": f"JSON parse алдаа: {str(je)}", "raw": raw[:500]}
        except Exception as e:
            error = f"Алдаа гарлаа: {str(e)}"'''

new_part = '''            try:
                result = json.loads(raw)
                # Python-д grand_total дахин тооцоолох
                mat_total = sum(
                    (item.get("qty") or 0) * (item.get("unit_price") or 0)
                    for item in result.get("materials", [])
                )
                lab_total = sum(
                    (item.get("qty") or 0) * (item.get("unit_price") or 0)
                    for item in result.get("labor", [])
                )
                tra_total = sum(
                    (item.get("qty") or 0) * (item.get("unit_price") or 0)
                    for item in result.get("transport", [])
                )
                oth_total = sum(
                    (item.get("qty") or 0) * (item.get("unit_price") or 0)
                    for item in result.get("other", [])
                )
                # AI-н тооцоо хэт бага бол est_grand_total ашиглах
                ai_grand = mat_total + lab_total + tra_total + oth_total
                if ai_grand < est_grand_total * 0.5:
                    # AI тооцоо буруу — урьдчилсан тооцоог ашиглах
                    grand = est_grand_total
                    mat_total = est_materials
                    lab_total = est_labor
                    tra_total = est_transport
                    oth_total = est_other
                else:
                    grand = ai_grand
                # material total-г item бүрт нэмэх
                for item in result.get("materials", []):
                    item["total"] = int((item.get("qty") or 0) * (item.get("unit_price") or 0))
                for item in result.get("labor", []):
                    item["total"] = int((item.get("qty") or 0) * (item.get("unit_price") or 0))
                for item in result.get("transport", []):
                    item["total"] = int((item.get("qty") or 0) * (item.get("unit_price") or 0))
                for item in result.get("other", []):
                    item["total"] = int((item.get("qty") or 0) * (item.get("unit_price") or 0))
                # summary шинэчлэх
                try:
                    area_num2 = float(area) if area != "мэдэгдэхгүй" else 1
                except:
                    area_num2 = 1
                result["summary"] = {
                    "materials_total": int(mat_total),
                    "labor_total": int(lab_total),
                    "transport_total": int(tra_total),
                    "other_total": int(oth_total),
                    "grand_total": int(grand),
                    "price_per_m2": int(grand / area_num2) if area_num2 > 0 else 0,
                    "duration_months": result.get("summary", {}).get("duration_months", 6),
                }
            except Exception as je:
                result = {"error": f"JSON parse алдаа: {str(je)}", "raw": raw[:500]}
        except Exception as e:
            error = f"Алдаа гарлаа: {str(e)}"'''

if old_part in content:
    print("FOUND - орлуулж байна...")
    content = content.replace(old_part, new_part, 1)
    with open(views_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("DONE - Python тооцоо нэмэгдлээ")
else:
    print("NOT FOUND - текст таарахгүй байна")