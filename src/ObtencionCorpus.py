import os
import PyPDF2

def pdf_to_text(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()

    return text

def create_corpus(pdf_folder_path):
    corpus = []
    
    for filename in os.listdir(pdf_folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(pdf_folder_path, filename)
            text = pdf_to_text(file_path)
            corpus.append(text)

    return corpus

def save_corpus(corpus, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for text in corpus:
            file.write(text + '\n')

# Ruta de la carpeta que contiene los archivos PDF
pdf_folder_path = './data'

# Crear el corpus
corpus = create_corpus(pdf_folder_path)

# Guardar el corpus en un archivo de texto
output_file = './data/corpus.txt'
save_corpus(corpus, output_file)

print(f"Corpus guardado en {output_file}")
