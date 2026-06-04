import os

# admin_sidebar tag файл хаана байна
for root, dirs, files in os.walk("."):
    for f in files:
        if "admin_sidebar" in f or "sidebar_registry" in f:
            print(os.path.join(root, f))

# _sidebar_registry.html файл хайх
for root, dirs, files in os.walk("templates"):
    for f in files:
        print(os.path.join(root, f))