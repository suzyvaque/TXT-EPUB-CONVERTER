## 🔌 TXT Converter

Converts a partially formatted txt to a clean version txt and a fully formatted epub.

### File Structure

**Supported Input File Format:**

📄 어떤 책 1.txt  
📄 어떤 책 2.txt  
📄 어떤 책 3.txt  
...

↓

**Output Directory Structure:**

📁 clean_txt/

├── [저자명] 어떤 책 1권.txt

├── [저자명] 어떤 책 2권.txt

├── [저자명] 어떤 책 3권.txt

...

📁 clean_epub/

├── [저자명] 어떤 책 1권.epub

├── [저자명] 어떤 책 2권.epub

├── [저자명] 어떤 책 3권.epub

...

## ✔️ Getting Started

1. Download [Calibre](https://calibre-ebook.com/download), used to convert .html to .epub via ebook-convert. After download and installation, it should be accessible at `C:/Program Files/Calibre2/ebook-convert.exe`.

2. Place raw `.txt` files in the `input` folder with names like:
   - `어떤 책 1.txt`
   - `어떤 책 2.txt`

3. Run `python txt_handler.py` in terminal.

4. Type in information in terminal.