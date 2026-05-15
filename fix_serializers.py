import io
path = r"apps\api\views.py"
with io.open(path, "r", encoding="utf-8") as f:
    text = f.read()
text = text.replace("S.GovernmentOrgSerializer", "S.GovernmentOrganizationSerializer")
text = text.replace("S.NonGovernmentOrgSerializer", "S.NonGovernmentOrganizationSerializer")
with io.open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("DONE")