from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
import os
import numpy as np

# Set your original dataset directory
original_dataset_dir = "D:/Topik Khusus SC & KG/road-marking/zebra crossing.v2i.coco/train"

# Set the directory to save augmented images
augmented_dir = "D:/Topik Khusus SC & KG/road-marking/zebra crossing.v2i.coco/augmented"

# Create the augmented images directory if it doesn't exist
if not os.path.exists(augmented_dir):
    os.makedirs(augmented_dir)

# Create an ImageDataGenerator instance with desired augmentations
datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# List all images in the original dataset directory
image_files = [f for f in os.listdir(original_dataset_dir) if f.endswith(".jpg")]

# Define the number of augmented images per original image
augmentation_factor = 5

print("start augmented...")
# Apply augmentation to each image
for image_file in image_files:
    image_path = os.path.join(original_dataset_dir, image_file)
    
    # Load the image and resize it to 416x416
    img = image.load_img(image_path, target_size=(416, 416))  # set target size to 416x416
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    
    # Generate augmented images
    i = 0
    for batch in datagen.flow(x, batch_size=1, save_to_dir=augmented_dir, save_prefix=image_file[:-4], save_format='jpg'):
        i += 1
        if i >= augmentation_factor:
            break

print("finish...")
# Set your dataset directory
# dataset_dir = "D:/Topik Khusus SC & KG/road-marking/zebra crossing.v2i.coco/train"

# Set the directory to save augmented images
# augmented_dir = "D:/Topik Khusus SC & KG/road-marking/zebra crossing.v2i.coco/augmented"

# Create the augmented images directory if it doesn't exist


    
