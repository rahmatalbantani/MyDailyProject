import os

def organize_files(input_folder):
    # Mendapatkan daftar file di folder input
    files = os.listdir(input_folder)

    for file in files:
        # Mengecek apakah item di dalam folder adalah file
        if os.path.isfile(os.path.join(input_folder, file)):
            # Mendapatkan nama file tanpa ekstensi
            file_name, file_extension = os.path.splitext(file)

            # Membuat nama folder dengan menambahkan "_report"
            folder_name = file_name + "_report"

            # Mengecek apakah folder sudah ada atau belum, jika belum maka membuatnya
            folder_path = os.path.join(input_folder, folder_name)
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

            # Memindahkan file ke dalam folder yang sesuai
            old_file_path = os.path.join(input_folder, file)
            new_file_path = os.path.join(folder_path, file)

            os.rename(old_file_path, new_file_path)
            print(f"File {file} dipindahkan ke dalam folder {folder_name}")

if __name__ == "__main__":
    # Mendapatkan current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    lokasifile = "Data/LaporanDownload/LaporanTerkenaCopas"
    inputfolder = os.path.join(current_directory, lokasifile) 
    # Melakukan organisasi file
    organize_files(inputfolder)
