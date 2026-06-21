import os
import re
import shutil

ROOT = r'e:\primer.com'

# Target folders and their new names
FOLDER_MAP = {
    '5f51aff01e95c4ec1baec2ef': 'assets_global',
    '68f68958c2668295d6501e97': 'assets_site',
    '69005831cbccd57cbcb253c9': 'assets_media',
}

HEX_PATTERN = re.compile(r'^[a-f0-9]{24}_')

def strip_hex(filename):
    """Strip webflow hex prefixes from filename."""
    original = filename
    while HEX_PATTERN.match(filename):
        filename = HEX_PATTERN.sub('', filename)
    if filename == '':
        filename = original  # Fallback if the whole name was hex
    return filename

def main():
    mappings = {}  # old_path_forward_slash -> new_path_forward_slash
    renames = []   # list of (old_abspath, new_abspath)

    for old_folder, new_folder in FOLDER_MAP.items():
        folder_path = os.path.join(ROOT, old_folder)
        if not os.path.isdir(folder_path):
            continue
        
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                old_filepath = os.path.join(root, filename)
                rel_dir = os.path.relpath(root, ROOT)
                
                # Compute new directory path string (relative)
                # First segment is old_folder, replace it with new_folder
                parts = rel_dir.split(os.sep)
                if parts[0] == old_folder:
                    parts[0] = new_folder
                new_rel_dir = '/'.join(parts)
                
                new_filename = strip_hex(filename)
                
                # Collision handling for the planned new name
                # We need to check if we already planned a file with this new path
                base_name, ext = os.path.splitext(new_filename)
                counter = 1
                candidate_rel_path = f"{new_rel_dir}/{new_filename}"
                
                while candidate_rel_path in mappings.values():
                    new_filename = f"{base_name}_{counter}{ext}"
                    candidate_rel_path = f"{new_rel_dir}/{new_filename}"
                    counter += 1
                
                old_rel_path = os.path.relpath(old_filepath, ROOT).replace(os.sep, '/')
                mappings[old_rel_path] = candidate_rel_path
                
                new_filepath = os.path.join(ROOT, os.path.normpath(candidate_rel_path))
                renames.append((old_filepath, new_filepath))

    # Also map the top-level folders themselves in case they are referenced as absolute paths in some generic way
    for old_folder, new_folder in FOLDER_MAP.items():
        mappings[old_folder + '/'] = new_folder + '/'
    
    # Sort mappings by length of old_path descending to prevent partial matches
    sorted_mappings = sorted(mappings.items(), key=lambda x: len(x[0]), reverse=True)
    
    # Update all references in codebase
    update_count = 0
    for root, dirs, files in os.walk(ROOT):
        # don't touch node_modules or .git if they exist
        if 'node_modules' in root or '.git' in root:
            continue
            
        for file in files:
            if file.endswith(('.html', '.htm', '.css', '.js')):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError:
                    continue
                
                new_content = content
                for old_p, new_p in sorted_mappings:
                    new_content = new_content.replace(old_p, new_p)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    update_count += 1

    print(f"Updated references in {update_count} files.")
    
    # Now physically rename the files and folders
    # First create all new directory structures
    for old_folder, new_folder in FOLDER_MAP.items():
        new_folder_path = os.path.join(ROOT, new_folder)
        os.makedirs(new_folder_path, exist_ok=True)
        
        # We need to recreate subdirectories
        old_folder_path = os.path.join(ROOT, old_folder)
        for dirpath, dirnames, filenames in os.walk(old_folder_path):
            rel_path = os.path.relpath(dirpath, old_folder_path)
            if rel_path != '.':
                target_dir = os.path.join(new_folder_path, rel_path)
                os.makedirs(target_dir, exist_ok=True)
                
    # Rename files
    rename_count = 0
    for old_path, new_path in renames:
        if os.path.exists(old_path):
            shutil.move(old_path, new_path)
            rename_count += 1
            
    print(f"Renamed {rename_count} files.")
    
    # Finally remove old empty directories
    for old_folder in FOLDER_MAP.keys():
        old_folder_path = os.path.join(ROOT, old_folder)
        if os.path.exists(old_folder_path):
            shutil.rmtree(old_folder_path)

if __name__ == '__main__':
    main()
