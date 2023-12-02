import os
import tkinter as tk
from tkinter import filedialog

def rename_files_in_directory(directory, delimiter, prefix_to_add):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # Split using the delimiter
            parts = filename.rsplit(delimiter, 1)
            if len(parts) == 2:
                new_filename = prefix_to_add + parts[1]
                new_path = os.path.join(directory, new_filename)
                os.rename(os.path.join(directory, filename), new_path)
                print(f'Renamed: {filename} to {new_filename}')

def process_directory(input_directory, output_directory, prefix_to_add):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_directory, input_directory)
    output_path = os.path.join(current_directory, output_directory)

    if not os.path.exists(input_path):
        print(f"Input directory does not exist: {input_path}")
        return

    if not os.path.exists(output_path):
        print(f"Output directory does not exist: {output_path}")
        return

    print(f"\n==> Processing files in directory: {input_path}")
    print(f"==> Saving renamed files to directory: {output_path}")

    rename_files_in_directory(input_path, '-', prefix_to_add)
    print('\n==> Finished Renaming!\n')

def main():
    root = tk.Tk()
    root.title("File Renamer")

    # Label dan Entry untuk input directory
    label_input_directory = tk.Label(root, text="Input Directory:")
    entry_input_directory = tk.Entry(root, width=50)
    entry_input_directory.insert(0, "Data/LaporanDownload")  # Set default input directory

    # Label dan Entry untuk output directory
    label_output_directory = tk.Label(root, text="Output Directory:")
    entry_output_directory = tk.Entry(root, width=50)
    entry_output_directory.insert(0, "Data/LaporanDownload")  # Set default output directory

    # Label dan Entry untuk prefix
    label_prefix = tk.Label(root, text="Prefix:")
    entry_prefix = tk.Entry(root, width=50)

    # Fungsi untuk menjalankan proses
    def run_process():
        process_directory(entry_input_directory.get(), entry_output_directory.get(), entry_prefix.get())

    # Tombol untuk menjalankan proses
    button_process = tk.Button(root, text="Process", command=run_process)

    # Menampilkan elemen-elemen GUI
    label_input_directory.grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)
    entry_input_directory.grid(row=0, column=1, pady=10, padx=10)
    
    label_output_directory.grid(row=1, column=0, pady=10, padx=10, sticky=tk.W)
    entry_output_directory.grid(row=1, column=1, pady=10, padx=10)
    
    label_prefix.grid(row=2, column=0, pady=10, padx=10, sticky=tk.W)
    entry_prefix.grid(row=2, column=1, pady=10, padx=10)

    button_process.grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
