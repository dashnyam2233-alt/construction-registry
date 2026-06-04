import os
# Admin nav template байгаа эсэх шалгах
for root, dirs, files in os.walk('templates'):
    for f in files:
        print(os.path.join(root, f))