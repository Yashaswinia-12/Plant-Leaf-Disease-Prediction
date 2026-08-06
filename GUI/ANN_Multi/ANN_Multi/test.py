from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os

model = load_model("my_model_ann.h5")
print("Loaded ANN model from disk.")

classs = {
    0: "Kingfisher",
    1: "Parrot",
    2: "Peacock",
    3: "Pigeon"
}

def classify(img_file):
    try:
        img = Image.open(img_file)
        img = img.resize((30, 30))
        img = np.array(img) / 255.0 
        img = np.expand_dims(img, axis=0)

        result = model.predict(img)
        class_index = np.argmax(result)
        prediction = classs[class_index]

        print(f"Predicted: {prediction} | File: {img_file}")
    except Exception as e:
        print(f"Error processing {img_file}: {e}")

path = 'my_dir/Test'
files = []

for r, d, f in os.walk(path):
    for file in f:
        if file.lower().endswith(('.jpeg', '.jpg', '.png')):
            files.append(os.path.join(r, file))

for f in files:
    classify(f)
    print()
