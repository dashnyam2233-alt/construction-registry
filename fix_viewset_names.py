import io
path = r"apps\api\views.py"
with io.open(path, "r", encoding="utf-8") as f:
    text = f.read()
text = text.replace("class GovernmentOrgViewSet", "class GovernmentOrganizationViewSet")
text = text.replace("class NonGovernmentOrgViewSet", "class NonGovernmentOrganizationViewSet")
with io.open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("DONE")