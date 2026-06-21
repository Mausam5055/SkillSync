import os, re

directory = r'e:\primer.com'
pattern = re.compile(r' integrity="sha384-[^"]+" crossorigin="anonymous"')
count = 0

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.html') or file.endswith('.htm'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            new_content = pattern.sub('', content)
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
print(f'Updated {count} files.')
