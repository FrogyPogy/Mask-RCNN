import os
from PIL import Image

def resize_images_in_folder(input_folder, output_folder, new_size):
    # Pastikan folder output sudah ada atau buat jika belum
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop melalui semua file dalam folder input
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Sesuaikan dengan ekstensi gambar yang ingin diubah
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Ubah dimensi gambar
            original_image = Image.open(input_path)
            resized_image = original_image.resize(new_size)

            # Simpan gambar yang telah diubah dimensi
            resized_image.save(output_path)


# Contoh penggunaan
input_folder_path = r'E:\Computer Vision\mrcnn2\dataset\before'  # Ganti dengan path folder input Anda
output_folder_path = r'E:\Computer Vision\mrcnn2\dataset\after'  # Ganti dengan path folder output untuk menyimpan gambar yang telah diubah dimensi
new_dimensions = (416, 416)

resize_images_in_folder(input_folder_path, output_folder_path, new_dimensions)