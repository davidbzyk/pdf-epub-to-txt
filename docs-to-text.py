import ebooklib.epub
import PyPDF2
import os

def epub_to_txt(epub_path, output_path):
    try:
        # Read the EPUB file
        book = ebooklib.epub.read_epub(epub_path)

        # Print the title if available
        title = book.get_metadata('DC', 'title')
        if title:
            print(f"Processing EPUB: {title[0][0]}")

        text_content = ""
        # Iterate through the items in the EPUB file and extract the text
        for item in book.items:
            if isinstance(item, ebooklib.epub.EpubHtml):
                text_content += item.get_body_content().decode("utf-8")

        # Write the text content to a .txt file
        with open(output_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text_content)

        # Delete the original EPUB file
        os.remove(epub_path)
        print(f"Converted {epub_path} to {output_path}")

    except Exception as e:
        print(f"Error processing {epub_path}: {e}")


def pdf_to_txt(pdf_path, output_path):
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfFileReader(pdf_file)
            text_content = ""

            # Iterate through all the pages and extract the text
            for page_num in range(reader.numPages):
                text_content += reader.getPage(page_num).extract_text()

            # Write the text content to a .txt file
            with open(output_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text_content)

            # Delete the original PDF file
            os.remove(pdf_path)
            print(f"Converted {pdf_path} to {output_path}")

    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")


# Directory containing EPUB and PDF files
input_directory = '/home/dave/Desktop/pdf-epub-to-txt/examples/aws-docs'

# Directory to save the output .txt files
output_directory = '/home/dave/Desktop/pdf-epub-to-txt/examples/to-text/'

# Iterate through all files in the input directory
for filename in os.listdir(input_directory):
    base_name, ext = os.path.splitext(filename)
    input_path = os.path.join(input_directory, filename)
    txt_filename = base_name + '.txt'
    txt_path = os.path.join(output_directory, txt_filename)

    if ext == '.epub':
        epub_to_txt(input_path, txt_path)
        print(f"Converted {filename} to {txt_filename}")
    elif ext == '.pdf':
        pdf_to_txt(input_path, txt_path)
        print(f"Converted {filename} to {txt_filename}")
