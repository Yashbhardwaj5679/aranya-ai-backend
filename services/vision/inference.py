import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image

# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Classes (same order as training)
class_names = [
    "aloe_vera",
    "amla",
    "ashwagandha",
    "bael",
    "brahmi",
    "giloy",
    "lemongrass",
    "neem",
    "turmeric",
    "tulsi"
]

# Load model
model = models.resnet18(weights=None)

num_features = model.fc.in_features
model.fc = nn.Linear(num_features, len(class_names))

model.load_state_dict(
    torch.load(
        "services/vision/models/aranya_model_best.pth",
        map_location=device
    )
)

model = model.to(device)
model.eval()

# Image transform
transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

def predict(image_path):

    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():

        outputs = model(image)
        probabilities = torch.softmax(outputs, dim=1)

        top_prob, top_class = torch.max(probabilities,1)

    predicted_class = class_names[top_class.item()]
    confidence = float(top_prob.item())

    if confidence < 0.75:
        return "not_medicinal_plant", confidence

    return predicted_class, confidence


# Test image
img_path = "services/vision/test_9.jpg"

plant, conf = predict(img_path)

print("Prediction:", plant)
print("Confidence:", round(conf,3))