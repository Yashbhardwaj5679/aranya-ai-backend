import os

data_dir = "data/kaggle_upload"

for cls in os.listdir(data_dir):
    path = os.path.join(data_dir, cls)
    if os.path.isdir(path):
        print(cls, len(os.listdir(path)))