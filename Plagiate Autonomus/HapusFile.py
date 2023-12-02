import os
import shutil



def delete_files_in_folders(folder_names):
    # Dapatkan direktori saat ini
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Tampilkan peringatan sebelum menghapus file di dalam folder
    


    # Loop melalui setiap nama folder yang diberikan
    for folder_name in folder_names:
        # Gabungkan direktori saat ini dengan nama folder
        folder_path = os.path.join(current_directory, folder_name)

        # Tanyakan konfirmasi hanya sekali sebelum memulai iterasi melalui file
        
            # Loop melalui semua file dalam folder dan hapus satu per satu
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"File {filename} dalam folder {folder_name} berhasil dihapus.")








def delete_folder_and_contents(folder_name):
    # Dapatkan direktori saat ini
    current_directory = os.path.dirname(os.path.abspath(__file__))
  # Gabungkan direktori saat ini dengan nama folder
    folder_path = os.path.join(current_directory, folder_name)

    # Tampilkan peringatan sebelum menghapus
    
    try:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
                print(f"File {item} dalam folder {folder_name} berhasil dihapus.")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Folder {item} dalam folder {folder_name} berhasil dihapus.")
    except FileNotFoundError:
        print(f"Folder {folder_name} tidak ditemukan.")
    

# Contoh penggunaan:
# Ganti 'Andi' dengan nama folder yang ingin Anda hapus isinya
confirm = input(f"Perhatian Anda Akan Mengahapus Item Download dan seluruh hasil plagiasi? (y/n): ").lower()

if confirm == 'y':
    delete_files_in_folders(['Data/LaporanDownload','Data/ExcelPart'])
    delete_folder_and_contents('Data/LaporanDownload/LaporanTerkenaCopas')
    delete_folder_and_contents('Data/OutputPlagiate')

else:
    print(f"Penghapusan isi folder dibatalkan.")

# Ganti ['folder1', 'folder2', ...] dengan daftar nama folder yang ingin Anda bersihkan

# Ganti 'NamaFolder' dengan nama folder yang ingin Anda hapus bersama isinya
