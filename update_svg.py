import os
import re

ROOT = r'e:\primer.com'

logo_svg_content = """<svg width="80" height="23" viewBox="0 0 80 23" fill="none" xmlns="http://www.w3.org/2000/svg">
<text x="0" y="18" font-family="sans-serif" font-weight="bold" font-size="20" fill="#1C212E" letter-spacing="-0.5">SkillSync.</text>
</svg>"""

with open(os.path.join(ROOT, 'Logo.svg'), 'w', encoding='utf-8') as f:
    f.write(logo_svg_content)

html_svg_content = """<svg width="100%" height="100%" viewBox="0 0 205 56" fill="none" xmlns="http://www.w3.org/2000/svg">
<text x="0" y="42" font-family="sans-serif" font-weight="bold" font-size="46" fill="#1C212E" letter-spacing="-1.5">SkillSync.</text>
</svg>"""

update_count = 0
# Regex to match the inline logo SVG block. 
pattern = re.compile(r'<svg width="100%" height="100%" view[B|b]ox="0 0 205 56" fill="none" xmlns="http://www\.w3\.org/2000/svg">\s*<path.*?</svg>', re.DOTALL)

for root, _, files in os.walk(ROOT):
    for f in files:
        if f.endswith(('.html', '.htm')):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                new_content = pattern.sub(html_svg_content, content)
                
                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    update_count += 1
            except Exception as e:
                pass

print(f"Updated {update_count} HTML files with the new SkillSync inline SVG logo.")
