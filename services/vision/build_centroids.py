import os
import torch
import json
import numpy as np
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader
import torch.nn as nn

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
DATA_DIR = "data/split/train" # your local train folder

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

dataset = datasets.ImageFolder(DATA_DIR, transform=transform)
loader = DataLoader(dataset, batch_size=32, shuffle=False)

# Load feature extractor
model = models.resnet18(weights=None)
model.fc = nn.Identity()

model.load_state_dict(torch.load(
    "services/vision/models/best_resnet18_aranya.pth",
    map_location=DEVICE
), strict=False)

model = model.to(DEVICE)
model.eval()

features_by_class = {i: [] for i in range(len(dataset.classes))}

with torch.no_grad():
    for images, labels in loader:
        images = images.to(DEVICE)
        feats = model(images)
        for feat, label in zip(feats, labels):
            features_by_class[label.item()].append(feat.cpu().numpy())

centroids = {}

for class_idx, feats in features_by_class.items():
    feats = np.stack(feats)
    centroid = np.mean(feats, axis=0)
    centroids[dataset.classes[class_idx]] = centroid.tolist()

with open("services/vision/centroids.json", "w") as f:
    json.dump(centroids, f)

print("Centroids saved.")