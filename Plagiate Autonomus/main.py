import subprocess
import os

# Dapatkan direktori saat ini
current_directory = os.path.dirname(os.path.abspath(__file__))

# Daftar skrip yang akan dijalankan secara berurutan
scripts_to_run = [
    "1_SeparateLink.py",
    "2_DeleteDuplicateValueExcel.py",
    "3_FileDownloader.py",
    "4_Word to PDF.py",
    "5_NameFileSplitter.py",
    "6_Plagiarism Checker.py",
    "7_AccuratePlagiarism.py",
    "8_Finalization.py",
]

# Fungsi untuk menjalankan skrip dan menunggu hingga selesai
def run_script(script):
    script_path = os.path.join(current_directory, script)
    process = subprocess.Popen(f"python \"{script_path}\"", shell=True)
    process.wait()

# Jalankan skrip secara berurutan
for script in scripts_to_run:
    print(f"Running script: {script}")
    run_script(script)

print("All scripts have been executed.")
