# tools/make_birth_soums.py
import json, os, re
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = os.path.join(BASE_DIR, "registry", "birth_soums.py")

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

UB_DISTRICT_CODES = ["BGD", "BZD", "CHD", "SHD", "SBD", "HUD", "ND", "BD", "BHD"]

SPARQL = """
SELECT ?soumLabel ?aimagLabel WHERE {
  ?soum wdt:P31 wd:Q1518096;
        wdt:P131 ?aimag.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "mn". }
}
"""

def clean_name(s: str) -> str:
    s = (s or "").strip()
    s = re.sub(r"\s+сум$", "", s, flags=re.IGNORECASE).strip()
    return s

def main():
    r = requests.get(
        "https://query.wikidata.org/sparql",
        params={"query": SPARQL},
        headers={"Accept": "application/sparql-results+json", "User-Agent": "construction_registry_mvp/1.0"},
        timeout=90,
    )
    r.raise_for_status()
    data = r.json()

    grouped = {code: [] for code, _ in CITY_CHOICES}
    grouped["UB"] = UB_DISTRICT_CODES[:]

    for row in data["results"]["bindings"]:
        aimag = row["aimagLabel"]["value"].strip()
        soum = row["soumLabel"]["value"].strip()

        if aimag == "Улаанбаатар":
            continue

        code = LABEL_TO_CODE.get(aimag)
        if not code:
            continue

        name = clean_name(soum)
        if name:
            grouped[code].append(name)

    for code in grouped:
        if code != "UB":
            grouped[code] = sorted(set(grouped[code]))

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("# registry/birth_soums.py\n")
        f.write("BIRTH_SOUMS = ")
        json.dump(grouped, f, ensure_ascii=False, indent=4)
        f.write("\n")

    print("OK wrote:", OUT_PATH)
    print("AR:", len(grouped.get("AR", [])), "UVS:", len(grouped.get("UVS", [])), "UB:", len(grouped.get("UB", [])))

if __name__ == "__main__":
    main()
