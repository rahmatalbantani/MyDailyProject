import os
import subprocess

# Dapatkan direktori saat ini (folder tempat skrip Python berada)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Nama file batch yang akan dijalankan
batch_file_name = "RunPlagiarism.bat"

# Buat path lengkap menuju file batch
batch_file_path = os.path.join(current_directory, batch_file_name)

# Pindah ke direktori tempat skrip Python berada
os.chdir(current_directory)

# Jalankan file batch menggunakan subprocess
subprocess.run([batch_file_path], shell=True, check=True)
