# tools/make_birth_soums.py
# Wikidata-аас Монголын бүх "soum" (district of Mongolia)-ыг татаж
# registry/birth_soums.py файл үүсгэнэ.

import json
import os
import re
import sys
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = os.path.join(BASE_DIR, "registry", "birth_soums.py")

# Танай models.py дээрх CITY_CHOICES-ийн "code -> label" (яг адилхан байхаар)
CITY_CHOICES = [
    ("UB", "Улаанбаатар"),
    ("AR", "Архангай"),
    ("BA", "Баян-Өлгий"),
    ("BY", "Баянхонгор"),
    ("BU", "Булган"),
    ("GA", "Говь-Алтай"),
    ("GD", "Говьсүмбэр"),
    ("DA", "Дархан-Уул"),
    ("DO", "Дорноговь"),
    ("DU", "Дорнод"),
    ("DZ", "Дундговь"),
    ("ZA", "Завхан"),
    ("OR", "Орхон"),
    ("UV", "Өвөрхангай"),
    ("OM", "Өмнөговь"),
    ("SU", "Сүхбаатар"),
    ("SE", "Сэлэнгэ"),
    ("TO", "Төв"),
    ("UVS", "Увс"),
    ("HO", "Ховд"),
    ("HU", "Хөвсгөл"),
    ("HE", "Хэнтий"),
]

LABEL_TO_CODE = {label: code for code, label in CITY_CHOICES}

# UB дүүргүүд чинь кодоор хадгалагдаж байсан (чи хүсвэл өөрчилж болно)
UB_DISTRICT_CODES = ["BGD", "BZD", "CHD", "SHD", "SBD", "HUD", "ND", "BD", "BHD"]

SPARQL = """
SELECT ?soumLabel ?aimagLabel WHERE {
  ?soum wdt:P31 wd:Q1518096;
        wdt:P131 ?aimag.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "mn,en". }
}
"""

def clean_name(name: str) -> str:
    name = (name or "").strip()
    # "сум" гэдэг үгийг төгсгөлөөс нь авч болно (сонголтоор)
    name = re.sub(r"\s+сум$", "", name, flags=re.IGNORECASE).strip()
    return name

def main():
    url = "https://query.wikidata.org/sparql"
    headers = {
        "Accept": "application/sparql-results+json",
        "User-Agent": "construction_registry_mvp/1.0 (local script)"
    }

    r = requests.get(url, params={"query": SPARQL}, headers=headers, timeout=60)
    r.raise_for_status()
    data = r.json()

    # Энд aimagLabel -> [soumName]
    grouped = {code: [] for code, _ in CITY_CHOICES}
    grouped["UB"] = UB_DISTRICT_CODES[:]  # УБ-г дүүргээр нь бэлэн тавина

    # Wikidata-аас ирсэн мөрүүдийг aimagLabel-ээр код руу хөрвүүлж хийе
    rows = data["results"]["bindings"]
    for row in rows:
        aimag_label = row.get("aimagLabel", {}).get("value", "").strip()
        soum_label = row.get("soumLabel", {}).get("value", "").strip()

        # УБ-г алгасна (УБ бол дүүргийн код ашиглана)
        if aimag_label == "Улаанбаатар":
            continue

        code = LABEL_TO_CODE.get(aimag_label)
        if not code:
            # Заримдаа aimag_label өөрөөр орж ирж болдог (анги, тайлбар гэх мэт)
            continue

        sname = clean_name(soum_label)
        if sname:
            grouped[code].append(sname)

    # Давхардал арилгаж, цэгцэлнэ
    for code in grouped:
        if code == "UB":
            continue
        uniq = sorted(set(grouped[code]))
        grouped[code] = uniq

    # Файл бичих
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("# registry/birth_soums.py\n")
        f.write("# AUTO-GENERATED. Edit if needed.\n\n")
        f.write("BIRTH_SOUMS = ")
        f.write(json.dumps(grouped, ensure_ascii=False, indent=4))
        f.write("\n")

    print("OK: wrote", OUT_PATH)
    # quick stats
    total = sum(len(v) for k, v in grouped.items() if k != "UB")
    print("Aimags:", len(grouped) - 1, "Soums:", total, "UB districts:", len(grouped["UB"]))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR:", e)
        sys.exit(1)
