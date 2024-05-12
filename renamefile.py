''' Author: @Najib Rifai
    Purpose: Rename file jpg    
'''
import os
from PIL import Image
import cv2

def rename_and_save_images(input_dir, output_dir):
    # Membuat direktori "train renamed" jika belum ada
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Daftar semua file dengan ekstensi .jpg di direktori input
    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.jpg')]

    for i, filename in enumerate(image_files, start=1):
        # Baca gambar
        image_path = os.path.join(input_dir, filename)
        image = Image.open(image_path)
        #change start value 
        init = 1300
        # Tentukan nama baru
        new_filename = f"imgTrainMR{init+i}.jpg"
        new_image_path = os.path.join(output_dir, new_filename)

        # Simpan gambar dengan nama baru
        image.save(new_image_path)
        
        print(f"Renaming: {filename} -> {new_filename}")
        

def resize_images(input_dir, output_dir, target_size=(416, 416)):
    # Pastikan direktori output sudah ada, jika belum, buat
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List semua file dalam direktori input
    file_list = os.listdir(input_dir)

    for filename in file_list:
        # Cek apakah file adalah gambar (jpeg atau png)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            # Baca gambar
            image = cv2.imread(input_path)

            # Resize gambar
            resized_image = cv2.resize(image, target_size)

            # Simpan gambar yang telah diresize
            cv2.imwrite(output_path, resized_image)

# Contoh penggunaan

if __name__ == "__main__":
    #pilih sesuai dengan direktori 
    input_directory = r"D:\Topik Khusus SC & KG\road-marking\zebra crossing.v2i.coco\augmented"
    output_directory = r"D:\Topik Khusus SC & KG\road-marking\zebra crossing.v2i.coco\train_renamed"

    rename_and_save_images(input_directory, output_directory)
