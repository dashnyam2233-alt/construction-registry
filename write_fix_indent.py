lines = open("apps/registry/views.py", "r", encoding="utf-8").readlines()
# 256-р мөр давхардсан — устгах
del lines[255]
open("apps/registry/views.py", "w", encoding="utf-8").writelines(lines)
print("OK")