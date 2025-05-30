import subprocess
import os
import shutil

EBOOK_CONVERT = 'C:/Program Files/Calibre2/ebook-convert.exe'

def remove_pycache(root_dir='.'):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            if dirname == '__pycache__':
                pycache_path = os.path.join(dirpath, dirname)
                shutil.rmtree(pycache_path)
                print(f"🗑️ Removed: {pycache_path}")

def convert_txt_to_epub(name, author, nums, cover_image=''):
    input_dir = '../input/formatted_txt'
    output_dir = '../output/clean_epub'
    os.makedirs(output_dir, exist_ok=True)
    for num in nums:
        txt_file = f'{input_dir}/[{author}] {name} {num}권.txt'
        html_file = f'{input_dir}/[{author}] {name} {num}권.html'
        epub_file = f'{output_dir}/[{author}] {name} {num}권.epub'
        title = f'{name} {num}권'

        if not os.path.exists(txt_file):
            print(f"⚠️ File not found: {txt_file}")
            continue

        # Read original txt content
        with open(txt_file, 'r', encoding='utf-8') as f:
            txt_content = f.read()

        # Create HTML wrapper with cover on page 1
        html_content = f"""<html>
<head><meta charset="utf-8"></head>
<body>

<!-- Cover page -->
<div style="text-align:center; page-break-after: always;">
  <img src="{cover_image}" alt="Cover" style="max-width:100%; height:auto;">
</div>

<!-- Main content -->
<pre style="font-family:inherit; white-space:pre-wrap;">
{txt_content}
</pre>

</body>
</html>
"""

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        # Convert HTML to EPUB
        cmd = [
            EBOOK_CONVERT,
            html_file,
            epub_file,
            '--title', title,
            '--authors', author
        ]

        if cover_image:
            cmd += ['--cover', cover_image]

        try:
            subprocess.run(cmd, check=True)
            print(f"✅ Converted file: {epub_file}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Conversion failed for {html_file}: {e}")


    if os.path.exists(input_dir):
        for filename in os.listdir(input_dir):
            file_path = os.path.join(input_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        os.rmdir(input_dir)
    remove_pycache()
    print("✅ Finished clean-up.")
    print("✅ Clean txt files saved in 'clean_txt' directory.")
    print("✅ Clean EPUB files saved in 'clean_epub' directory.")