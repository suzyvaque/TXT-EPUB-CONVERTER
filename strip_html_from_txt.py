import re
import os

def fix_unclosed_tags(text: str) -> str:
    lines = text.splitlines(keepends=True)
    fixed_lines = []

    for line in lines:
        if '<span' in line and '</span>' not in line:
            line = line.rstrip('\n') + '</span>\n'
        if '<div' in line and '</div>' not in line:
            line = line.rstrip('\n') + '</div>\n'
        fixed_lines.append(line)

    return ''.join(fixed_lines)

def strip_html_tags(text: str) -> str:
    return re.sub(r'<[^>]+>', '', text)

def strip_html_from_txt(name, author, nums):
    output_dir = 'clean_txt'
    os.makedirs(output_dir, exist_ok=True)

    for num in nums:
        input_file = f'{name} {num}.txt'
        output_file = f'{output_dir}/[{author}] {name} {num}권.txt'

        if not os.path.exists(input_file):
            print(f"⚠️ File not found: {input_file}")
            continue

        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Fix unclosed tags
        content = fix_unclosed_tags(content)

        # 2. Strip all HTML tags
        content = strip_html_tags(content)

        # 3. Save cleaned text
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ Saved clean txt files: {output_file}")
