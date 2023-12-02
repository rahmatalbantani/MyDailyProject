import pandas as pd
import os

# Membaca file Excel
current_directory = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_directory,'Data/ExcelPart/data.xlsx')
df = pd.read_excel(path)

# Misalnya, kita ingin memisahkan nilai di kolom 'Nama' yang memiliki koma
# dan membuat baris baru untuk setiap nilai yang terpisah
df['Link'] = df['Link'].str.split(', ')

# Mengonversi nilai yang terpisah menjadi baris baru
df = df.explode('Link')
# Menyimpan DataFrame yang diperbarui ke file Excel baru
path2 = os.path.join(current_directory,'Data/ExcelPart/updateddata.xlsx')
df.to_excel(path2, index=False)
