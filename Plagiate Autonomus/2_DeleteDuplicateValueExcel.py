import pandas as pd
import os
# Baca file Excel
current_directory = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_directory,'Data/ExcelPart/updateddata.xlsx')
df = pd.read_excel(path)

# Menghilangkan duplikat berdasarkan kolom 'NIM'
df = df.drop_duplicates(subset='NIM', keep='first')

# Menyimpan hasil ke file Excel baru
path2 = os.path.join(current_directory,'Data/ExcelPart/input.xlsx')
df.to_excel(path2, index=False)
