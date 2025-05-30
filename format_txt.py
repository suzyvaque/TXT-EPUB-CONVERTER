import re
import os

def fix_unclosed_tags(text: str) -> str:
    lines = text.splitlines(keepends=True)
    fixed_lines = []

    for line in lines:
        # Replace <span ...> with HTML that EPUB understands
        line = re.sub(
            r'<span[^>]*>',
            '<span style="color:maroon; font-weight:bold;">',
            line
        )

        # Ensure closing span exists
        if '</span>' in line:
            line = line.replace('</span>', '</span>')
        elif '<span style="color:maroon; font-weight:bold;">' in line:
            # Auto-close the span if it was opened but not closed
            line = line.rstrip('\n') + '</span>\n'

        # Fix unclosed <div>
        if '<div' in line and '</div>' not in line:
            line = line.rstrip('\n') + '</div>\n'

        fixed_lines.append(line)

    return ''.join(fixed_lines)


def format_txt(name, author, nums):
    output_dir = 'formatted_txt'
    os.makedirs(output_dir, exist_ok=True)
    for num in nums:
        input_file = f'{name} {num}.txt'
        output_file = f'{output_dir}/[{author}] {name} {num}권.txt'

        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Step 1: Convert <h1> episode headers to <h2> and add IDs
        episode_pattern = rf'<h1[^>]*>\s*{re.escape(name)}\s*(\d+화)[^\n<]*'
        def replace_header(match):
            episode_num = match.group(1)
            episode_id = 'ep' + re.sub(r'\D', '', episode_num)  # ep205, ep001, etc.
            return f'<h2 id="{episode_id}" style="text-align:center;font-size:20px;">{episode_num}</h2>\n'

        updated_content = re.sub(episode_pattern, replace_header, content, flags=re.IGNORECASE | re.DOTALL)

        # Step 2: Fix unclosed tags
        updated_content = fix_unclosed_tags(updated_content)

        # Step 3: Generate TOC links
        episodes = re.findall(r'<h2 id="(ep\d+)"[^>]*>(\d+화)</h2>', updated_content)
        toc_links = ''.join([f'<a href="#{eid}">{title}</a><br>\n' for eid, title in episodes])

        toc_block = f'<div style="page-break-after: always;">\n<h3>목차</h3>\n{toc_links}</div>\n\n'

        # Step 4: Add main header, author, TOC
        header_block = (
            f'<h1 style="text-align:center;font-size:24px;">{name} {num}권</h1>\n\n'
            f'<h3 style="text-align:center;font-size:16px;">{author}</h3>\n'
            f'<div style="page-break-after: always;"></div>\n\n'
        )

        full_output = header_block + toc_block + updated_content

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_output)
