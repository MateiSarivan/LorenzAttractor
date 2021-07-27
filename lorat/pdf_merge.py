import PyPDF2
import os

def merge_pdfs(address, pdf_name):

    pdf_files_handlers = []
    pdf_files = []
    pdf_file_addresses = []
    for fl in os.listdir(address):
        if ".pdf" in fl:
            pdf_address = os.path.join(address, fl)
            pdf_file_addresses.append(pdf_address)
            pdf_file_handler = open(pdf_address, 'rb')
            pdf_files_handlers.append(pdf_file_handler)
            pdf_files.append(PyPDF2.PdfFileReader(pdf_file_handler))

    pdfWriter = PyPDF2.PdfFileWriter()

    for pdf_file in pdf_files:
        for pageNum in range(pdf_file.numPages):
            pageObj = pdf_file.getPage(pageNum)
            pdfWriter.addPage(pageObj)


    pdfOutputFile = open(os.path.join(address, pdf_name + '.pdf'), 'wb')
    pdfWriter.write(pdfOutputFile)

    pdfOutputFile.close()
    for pdf_file_handler in pdf_files_handlers:
        pdf_file_handler.close()


    for pdf_file_address in pdf_file_addresses:
        os.remove(pdf_file_address)

