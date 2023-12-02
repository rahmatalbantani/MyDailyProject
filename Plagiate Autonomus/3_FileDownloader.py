import os
from typing import List
import pandas as pd
from gdown import download

def google_drive_bulk_download(input_excel_file_name: str = "Data/ExcelPart/input.xlsx", output_directory_name: str = "Data/LaporanDownload") -> List[str]:
    messages = []  # List to store informational messages

    current_directory = os.path.dirname(os.path.abspath(__file__))
    input_excel_file_path = os.path.join(current_directory, input_excel_file_name)
    output_directory_path = os.path.join(current_directory, output_directory_name)

    try:
        df = pd.read_excel(input_excel_file_path)
    except FileNotFoundError:
        messages.append(f"\n!!! The File '{input_excel_file_path}' is Invalid!\n")
        return messages

    try:
        os.makedirs(output_directory_path, exist_ok=True)
        os.chdir(output_directory_path)
    except FileNotFoundError:
        messages.append(f"\n!!! The Directory '{output_directory_path}' is Invalid!\n")
        return messages

    file_lines_count = len(df)
    messages.append('\n\n==> Started Downloading!\n')

    for i, row in df.iterrows():
        nama = row['Nama']
        download_url = row['Link']

        messages.append(f'\n-> Downloading {nama}... [{i + 1}/{file_lines_count}]')

        try:
            download(url=download_url, quiet=False, fuzzy=True)
        except Exception as e:
            messages.append(f"!!! Error downloading {nama}: {str(e)}")

        messages.append('Finished!')

    messages.append('\n\n==> Finished Downloading!')
    return messages

if __name__ == "__main__":
    output_messages = google_drive_bulk_download()
    for message in output_messages:
        print(message)
