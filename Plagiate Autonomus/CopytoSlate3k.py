import os
import shutil

def copy_file_to_destination(source_file, destination_directory):


    # Membuat direktori tujuan jika belum ada
    os.makedirs(destination_directory, exist_ok=True)
    
    # Menyusun path lengkap file tujuan
    # Cek apakah file tujuan sudah ada
    if os.path.exists(destination_directory + "\classes.py"):
        # Tanyakan konfirmasi untuk menggantikan file
        user_input = input(f"File {os.path.basename(source_file)} sudah ada. Apakah Anda ingin menggantikannya? (y/n): ").lower()

        if user_input != 'y':
            print("Proses dibatalkan.")
            return

    # Menyalin file
    shutil.copy2(source_file, destination_directory)
    print(f"File berhasil disalin ke: {destination_directory}")

if __name__ == "__main__":
    # Ganti path file sumber sesuai dengan kebutuhan Anda
    current_directory = os.path.dirname(os.path.abspath(__file__))
    source_file_path = os.path.join(current_directory,'classes.py')
    path1 = r"C:\Users"
    path2 = os.getlogin()
    path3 = r"AppData\Local\Programs\Python\Python310\Lib\site-packages\slate3k"
    pathfinal = os.path.join(path1,path2,path3)

    # Ganti direktori tujuan sesuai dengan kebutuhan Anda
    #destination_directory = r"D:\\Game"

    copy_file_to_destination(source_file_path, pathfinal)
