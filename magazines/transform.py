import os
from pymupdf4llm import to_markdown

# Directory containing the PDF files
PDF_DIRECTORY = "/home/magazines"
MD_OUTPUT_DIRECTORY = "/home/frontend/src/content/magazines/"

# Ensure the output directory exists
os.makedirs(MD_OUTPUT_DIRECTORY, exist_ok=True)

def convert_pdf_to_md(pdf_file, output_dir):
    try:
        # Generate the output markdown file path
        md_filename = os.path.splitext(os.path.basename(pdf_file))[0] + ".md"
        md_file_path = os.path.join(output_dir, md_filename)

        # Convert PDF to Markdown
        markdown_text = to_markdown(pdf_file)

        # Write the markdown content to the output file
        with open(md_file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(markdown_text)

        print(f"Successfully converted {pdf_file} to {md_file_path}")
    except Exception as e:
        print(f"Failed to convert {pdf_file}: {e}")

def main():
    # List all PDF files in the directory
    pdf_files = [os.path.join(PDF_DIRECTORY, f) for f in os.listdir(PDF_DIRECTORY) if f.endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found in the directory.")
        return

    # Convert each PDF file to Markdown
    for pdf_file in pdf_files:
        convert_pdf_to_md(pdf_file, MD_OUTPUT_DIRECTORY)

if __name__ == "__main__":
    main()
