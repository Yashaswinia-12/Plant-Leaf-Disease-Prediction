import os
from PIL import Image

image_dir = "my_dir/Pigeons"

for filename in os.listdir(image_dir):
    file_path = os.path.join(image_dir, filename)

    try:
        with Image.open(file_path) as img:
            rgb_img = img.convert("RGB")
            new_filename = os.path.splitext(filename)[0] + ".jpg"
            new_path = os.path.join(image_dir, new_filename)
            rgb_img.save(new_path, "JPEG", quality=95)

        
        if not filename.lower().endswith(".jpg"):
            os.remove(file_path)

    except Exception as e:
        print(f"Skipping {filename}: {e}")
