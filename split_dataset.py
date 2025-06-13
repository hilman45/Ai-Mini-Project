import os
import shutil
import random

SOURCE_DIR = 'standardized_images'
DEST_DIR = 'dataset'
SPLIT = [0.7, 0.15, 0.15]  # Train, Val, Test

random.seed(42)

for breed in os.listdir(SOURCE_DIR):
    images = os.listdir(os.path.join(SOURCE_DIR, breed))
    random.shuffle(images)

    total = len(images)
    train_end = int(SPLIT[0] * total)
    val_end = train_end + int(SPLIT[1] * total)

    split_names = ['train', 'val', 'test']
    split_data = [images[:train_end], images[train_end:val_end], images[val_end:]]

    for split_name, split_images in zip(split_names, split_data):
        split_path = os.path.join(DEST_DIR, split_name, breed)
        os.makedirs(split_path, exist_ok=True)
        for img in split_images:
            src = os.path.join(SOURCE_DIR, breed, img)
            dst = os.path.join(split_path, img)
            shutil.copyfile(src, dst)
