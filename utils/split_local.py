import os
import random
import shutil

RAW_DIR = "data/raw"
SPLIT_DIR = "data/split"

TRAIN_DIR = os.path.join(SPLIT_DIR, "train")
VAL_DIR = os.path.join(SPLIT_DIR, "val")

if os.path.exists(SPLIT_DIR):
    shutil.rmtree(SPLIT_DIR)

os.makedirs(TRAIN_DIR)
os.makedirs(VAL_DIR)

classes = []

for c in os.listdir(RAW_DIR):
    class_path = os.path.join(RAW_DIR, c)
    if os.path.isdir(class_path):
        images = [f for f in os.listdir(class_path)
                  if f.lower().endswith((".jpg", ".jpeg", ".png"))]
        if len(images) > 0:
            classes.append(c)

for cls in classes:
    os.makedirs(os.path.join(TRAIN_DIR, cls))
    os.makedirs(os.path.join(VAL_DIR, cls))

    images = os.listdir(os.path.join(RAW_DIR, cls))
    random.shuffle(images)

    split_point = int(0.8 * len(images))

    train_imgs = images[:split_point]
    val_imgs = images[split_point:]

    for img in train_imgs:
        shutil.copy(
            os.path.join(RAW_DIR, cls, img),
            os.path.join(TRAIN_DIR, cls, img)
        )

    for img in val_imgs:
        shutil.copy(
            os.path.join(RAW_DIR, cls, img),
            os.path.join(VAL_DIR, cls, img)
        )

print("Local split complete.")