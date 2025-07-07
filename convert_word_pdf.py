import pythoncom
import win32com.client

def convert_word_to_pdf(word_file, pdf_file):
    pythoncom.CoInitialize()  # Initialise COM dans ce thread
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    doc = word.Documents.Open(word_file)
    try:
        wdExportFormatPDF = 17
        doc.ExportAsFixedFormat(OutputFileName=pdf_file, ExportFormat=wdExportFormatPDF)
    finally:
        doc.Close(False)
        word.Quit()