from pypdf import PdfReader

class PDFLoader:
    """
    Responsible only for reading PDFs and returning raw text.
    Single Responsibility Principle.
    """
    def __init__(self, file_path:str):
        self.file_path = file_path

    def load(self) ->str:
        """
        Reads the PDF file and returns the raw text.
        """
        reader = PdfReader(self.file_path)
        pages = []
        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text() 

            if text:
                pages.append(text)
            else:
                print(f"Warning: No text found on page {page_number} of {self.file_path}")  
        # for page_number, page in enumerate(reader.pages, start=1):

        #     text = page.extract_text()

        #     print("PAGE:", page_number)
        #     print(repr(text))
        return "\n".join(pages)

    