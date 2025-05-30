from format_txt import format_txt
from strip_html_from_txt import strip_html_from_txt
from convert_txt_to_epub import convert_txt_to_epub



print("""

==============================
START CONVERTING TXT TO EPUB!
==============================

Input file format:
📄 어떤 책 1.txt  
📄 어떤 책 2.txt  
...

↓

📁 clean_txt/
├── [저자명] 어떤 책 1권.txt
├── [저자명] 어떤 책 2권.txt
...
📁 clean_epub/
├── [저자명] 어떤 책 1권.epub
├── [저자명] 어떤 책 2권.epub
...\n
""")


print("\n⭐ Book Title --- e.g., Book Title : 어떤 책")
name = input("   Book Title : ").strip()
print("\n⭐ Author Name --- e.g., Author Name : 저자 이름")
author = input("   Author Name : ").strip()
print("\n⭐ Number of Files --- e.g., Number of Files : 4")
total_nums = int(input("   Number of Files : ").strip())
print("\n⭐ Cover Image with Extension .jpg/.png --- Cover Image : cover.png")
print("   If none, just press enter to pass.")
cover_image = input("   Cover Image : ").strip()



nums = [_ for _ in range(1, total_nums+1)]

strip_html_from_txt(name, author, nums)
format_txt(name, author, nums)
convert_txt_to_epub(name, author, nums, cover_image)
