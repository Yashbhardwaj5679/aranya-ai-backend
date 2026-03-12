import os
import torch
import numpy as np
from PIL import Image
from torchvision import models, transforms
from sklearn.metrics.pairwise import cosine_similarity

IMAGE_DIR = "data/raw/turmeric"   # change per plant
SIM_THRESHOLD = 0.92           # similarity threshold

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Pretrained model
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
model.fc = torch.nn.Identity()
model = model.to(device)
model.eval()

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

embeddings = []
image_paths = []

print("Extracting features...")

for img_name in os.listdir(IMAGE_DIR):
    if img_name.lower().endswith((".jpg",".jpeg",".png")):
        path = os.path.join(IMAGE_DIR, img_name)

        try:
            img = Image.open(path).convert("RGB")
            img = transform(img).unsqueeze(0).to(device)

            with torch.no_grad():
                feat = model(img).cpu().numpy()

            embeddings.append(feat[0])
            image_paths.append(path)

        except:
            continue

embeddings = np.array(embeddings)

print("Checking similarity...")

keep = []
removed = []

for i in range(len(embeddings)):
    if len(keep) == 0:
        keep.append(i)
        continue

    sim = cosine_similarity([embeddings[i]], embeddings[keep])[0]

    if np.max(sim) < SIM_THRESHOLD:
        keep.append(i)
    else:
        removed.append(image_paths[i])

print("Removing similar images...")

for path in removed:
    os.remove(path)

print(f"Kept {len(keep)} images")
print(f"Removed {len(removed)} duplicates")