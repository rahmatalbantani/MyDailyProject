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



def process_directory(directory, entry_prefix):
    delimiter = '-'
    prefix_to_add = entry_prefix  # Get the prefix from the entry field
    rename_files_in_directory(directory, delimiter, prefix_to_add)

current_directory = os.path.dirname(os.path.abspath(__file__))
output = "Data/LaporanDownload"
input = os.path.join(current_directory, output)
entry_prefix = ""

def main():
    process_directory(input, entry_prefix)


if __name__ == "__main__":
    main()
