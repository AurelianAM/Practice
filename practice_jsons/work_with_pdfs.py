import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfFileReader, PdfFileWriter

def unite_pdfs():
    pdf_writer = PdfFileWriter()
    files = filedialog.askopenfilenames(filetypes=[('PDF Files', '*.pdf')])
    for file in files:
        pdf_reader = PdfFileReader(file)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open('united.pdf', 'wb') as out:
        pdf_writer.write(out)

def split_pdf():
    file = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
    pdf = PdfFileReader(file)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        with open(f'split_page_{page}.pdf', 'wb') as out:
            pdf_writer.write(out)

def add_pdf():
    file1 = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
    file2 = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
    pdf_writer = PdfFileWriter()
    for file in [file1, file2]:
        pdf_reader = PdfFileReader(file)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open('added.pdf', 'wb') as out:
        pdf_writer.write(out)

root = tk.Tk()
btn_unite = tk.Button(root, text="Unite PDFs", command=unite_pdfs)
btn_split = tk.Button(root, text="Split PDF", command=split_pdf)
btn_add = tk.Button(root, text="Add PDF", command=add_pdf)
btn_unite.pack()
btn_split.pack()
btn_add.pack()
root.mainloop()
