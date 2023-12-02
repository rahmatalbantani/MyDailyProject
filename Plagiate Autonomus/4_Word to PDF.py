import os
from docx2pdf import convert
from tqdm import tqdm

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def convert_docx_to_pdf(input_folder, output_folder):
    converted_files = set()  # Set untuk melacak file yang sudah dikonversi

    for root, dirs, files in os.walk(input_folder):
        for file in tqdm(files, desc="Mengonversi", unit="file"):
            input_file_path = os.path.join(root, file)
            output_file_path = os.path.join(output_folder, file.replace(".docx", ".pdf"))

            if os.path.exists(output_file_path):
                tqdm.write(f"File {file} sudah ada di {output_folder}. Melewati...")
                continue

            try:
                convert(input_file_path, output_folder)
                converted_files.add(file)
                tqdm.write(f"{file} berhasil dikonversi. Disimpan di {output_folder}.")

                # Hapus file Word setelah konversi berhasil
                os.remove(input_file_path)
                tqdm.write(f"File {file} berhasil dihapus.")
            except Exception as e:
                tqdm.write(f"Terjadi kesalahan saat mengonversi {file}: {e}")

    return converted_files

if __name__ == "__main__":
    # Menggunakan current directory sebagai basis
    current_directory = os.path.dirname(os.path.abspath(__file__))


    # Menambahkan subfolder untuk input dan output
    input_subfolder = "Data/LaporanDownload"
    output_subfolder = "Data/LaporanDownload"

    input_folder_path = os.path.join(current_directory, input_subfolder)
    output_folder_path = os.path.join(current_directory, output_subfolder)

    # Membuat subfolder jika belum ada
    create_folder(input_folder_path)
    create_folder(output_folder_path)

    converted_files = convert_docx_to_pdf(input_folder_path, output_folder_path)

    if converted_files:
        print("\nFile yang berhasil dikonversi:")
        for file in converted_files:
            print(file)
    else:
        print("\nTidak ada file yang berhasil dikonversi.")

    # Cetak full path dari direktori yang digunakan
    print(f"\nInput Folder: {os.path.abspath(input_folder_path)}")
    print(f"Output Folder: {os.path.abspath(output_folder_path)}")
