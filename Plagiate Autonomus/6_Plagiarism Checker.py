import os
import shutil
import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF
from docx import Document
import webbrowser


def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        pdf_document = fitz.open(pdf_path)

        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text += page.get_text()

        pdf_document.close()
    except fitz.fitz.EmptyFileError:
        print(f"Warning: Empty PDF file encountered - {pdf_path}")
    return text


def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    return text


def preprocess_text(text):
    return text.lower()


def tokenize_text(text):
    return text.split()


def jaccard_similarity(file1_tokens, file2_tokens):
    intersection = len(set(file1_tokens) & set(file2_tokens))
    union = len(set(file1_tokens) | set(file2_tokens))
    similarity = intersection / union
    return similarity


def check_plagiarism(file1_path, file2_path, min_word_limit=5):
    if file1_path.endswith('.pdf'):
        content1 = extract_text_from_pdf(file1_path)
    elif file1_path.endswith('.docx'):
        content1 = extract_text_from_docx(file1_path)
    else:
        raise ValueError("Unsupported file format for file1")

    tokens1 = tokenize_text(preprocess_text(content1))

    if file2_path.endswith('.pdf'):
        content2 = extract_text_from_pdf(file2_path)
    elif file2_path.endswith('.docx'):
        content2 = extract_text_from_docx(file2_path)
    else:
        raise ValueError("Unsupported file format for file2")

    tokens2 = tokenize_text(preprocess_text(content2))

    if len(tokens1) < min_word_limit or len(tokens2) < min_word_limit:
        return 0, ""  # Tidak dianggap plagiat jika kurang dari batas minimum kata

    similarity = jaccard_similarity(tokens1, tokens2)
    return similarity, content1, content2


def generate_html_report(results):
    html_content = "<html><head><title>Plagiarism Report</title>"
    # Tambahkan gaya CSS untuk menyorot kalimat yang sama
    html_content += "<style>.highlight { background-color: #87CEEB; }</style>"
    html_content += "</head><body>"

    # Tambahkan daftar hasil plagiasi untuk navigasi
    html_content += "<h1>Plagiarism Results:</h1><ul>"
    for result in results:
        file1_name, file2_name, similarity, _, _ = result
        anchor = f'similarity_{file1_name}_{file2_name}'
        # Hanya tambahkan hasil yang di atas threshold
        if similarity > 0.63:  # Ganti threshold sesuai kebutuhan
            html_content += f"<li><a href='#{anchor}'>Similarity between {file1_name} and {file2_name}</a></li>"
    html_content += "</ul>"

    # Tambahkan daftar nama file yang terkena plagiasi (tanpa duplikasi)
    html_content += "<h2>Files Indicated in Plagiarism:</h2>"
    html_content += "<ul>"

    # Gunakan set untuk menyimpan nama file yang sudah terindikasi
    unique_indicated_files = set()

    for result in results:
        file1_name, file2_name, similarity, _, _ = result
        if similarity > 0.63:  # Ganti threshold sesuai kebutuhan
            # Tambahkan ke set hanya jika belum ada
            if file1_name not in unique_indicated_files:
                html_content += f"<li>{file1_name}</li>"
                unique_indicated_files.add(file1_name)
            if file2_name not in unique_indicated_files:
                html_content += f"<li>{file2_name}</li>"
                unique_indicated_files.add(file2_name)
    html_content += "</ul>"

    for result in results:
        file1_name, file2_name, similarity, content1, content2 = result

        # Tambahkan anchor untuk navigasi
        anchor = f'similarity_{file1_name}_{file2_name}'
        # Hanya tambahkan hasil yang di atas threshold
        if similarity > 0.63:  # Ganti threshold sesuai kebutuhan
            html_content += f"<a name='{anchor}'></a>"

            html_content += f"<div style='border: 1px solid #ccc; padding: 10px; margin-bottom: 20px;'>"
            html_content += f"<h2>Similarity between {file1_name} and {file2_name}: {similarity}</h2>"

            # Tambahkan tombol navigasi
            prev_anchor = f'similarity_{results[results.index(result) - 1][0]}_{results[results.index(result) - 1][1]}' if results.index(result) > 0 else ''
            next_anchor = f'similarity_{results[results.index(result) + 1][0]}_{results[results.index(result) + 1][1]}' if results.index(result) < len(results) - 1 else ''

            html_content += f"<div style='text-align: center; margin-bottom: 10px;'>"
            if prev_anchor:
                html_content += f"<a href='#{prev_anchor}'>&lt;&lt; Previous</a> | "
            if next_anchor:
                html_content += f"<a href='#{next_anchor}'>Next &gt;&gt;</a>"
            html_content += "</div>"

            # Tambahkan struktur HTML untuk menampilkan file di sisi kiri dan kanan
            html_content += "<div style='display: flex; justify-content: space-between;'>"
            html_content += f"<div style='width: 48%; padding-right: 2%;'><h3>{file1_name}</h3>{highlight_plagiarism(content1, content2)}</div>"
            html_content += f"<div style='width: 48%; padding-left: 2%;'><h3>{file2_name}</h3>{highlight_plagiarism(content2, content1)}</div>"
            html_content += "</div>"

            html_content += "</div>"

    html_content += "</body></html>"
    return html_content


def highlight_plagiarism(text, reference_text):
    highlighted_text = text
    for sentence in text.split('. '):
        if sentence in reference_text:
            highlighted_text = highlighted_text.replace(sentence, f"<span class='highlight'>{sentence}</span>")
    return highlighted_text


def find_plagiarism(folder_path, threshold=0.63, min_word_limit=5):
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.pdf') or f.endswith('.docx')]

    results = []

    total_files = len(file_list)
    file_count = 0
    detected_plagiarism_count = 0

    for i in range(total_files):
        for j in range(i + 1, total_files):
            file_count += 1
            print(f"Processing file pair {file_count}/{total_files * (total_files - 1) / 2}")
            print(f"Testing plagiarism for: {file_list[i]} and {file_list[j]}")

            file1_name = file_list[i]
            file2_name = file_list[j]
            file1_path = os.path.join(folder_path, file1_name)
            file2_path = os.path.join(folder_path, file2_name)

            similarity, content1, content2 = check_plagiarism(file1_path, file2_path, min_word_limit)

            if similarity > threshold:
                detected_plagiarism_count += 1

                # Salin file yang terkena plagiat ke folder "LaporanTerkenaCopas"
                output_folder = os.path.join(folder_path, "LaporanTerkenaCopas")
                os.makedirs(output_folder, exist_ok=True)

                shutil.copy(file1_path, output_folder)
                shutil.copy(file2_path, output_folder)

                print(f"File {file1_name} and {file2_name} copied to: {output_folder}")

            results.append((file1_name, file2_name, similarity, content1, content2))
            print(f"Pairs tested: {file_count}, Detected plagiarism: {detected_plagiarism_count}")

    return results


def choose_folder(title="Select Folder"):
    root = tk.Tk()
    root.withdraw()

    folder_path = filedialog.askdirectory(title=title)
    return folder_path


# Example usage
current_directory = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(current_directory, "Data/LaporanDownload")

if input_folder:
    plagiarism_results = find_plagiarism(input_folder, min_word_limit=5)

    if plagiarism_results:
        output_folder = choose_folder(title="Pilih Folder Output Plagiarism Report")

        if output_folder:
            html_report = generate_html_report(plagiarism_results)

            output_path = os.path.join(output_folder, "plagiarism_report.html")

            with open(output_path, "w", encoding="utf-8") as html_file:
                html_file.write(html_report)

            webbrowser.open(output_path, new=2)
            print(f"Plagiarism report generated and opened. Location: {output_path}")
        else:
            print("No output folder selected. Exiting.")
    else:
        print("No plagiarism detected.")
else:
    print("No input folder selected. Exiting.")
