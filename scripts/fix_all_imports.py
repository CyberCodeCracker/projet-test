# fix_all_imports.py
import os
import re

def fix_file_imports(filepath):
    """Remove src. prefix from imports in a file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Remove src. prefix from imports
    content = re.sub(r'from src\.', 'from ', content)
    content = re.sub(r'import src\.', 'import ', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

print("="*80)
print("FIXING ALL FILES WITH 'src.' IMPORTS")
print("="*80)

# Files that need fixing (from your output)
files_to_fix = [
    "src/pages/admin_clients_page.py",
    "src/pages/base_page.py",
    "src/pages/categories_page.py",
    "src/pages/checkout_page.py",
    "src/pages/login_page.py",
    "src/pages/menu_details_page.py",
    "src/pages/menu_page.py",
    "src/pages/items_page.py",
    "src/tests/unit_tests.py"
]

fixed_count = 0

for filepath in files_to_fix:
    if os.path.exists(filepath):
        if fix_file_imports(filepath):
            print(f"✅ Fixed: {filepath}")
            fixed_count += 1
        else:
            print(f"⚠ Already clean: {filepath}")
    else:
        print(f"❌ Not found: {filepath}")

print(f"\nTotal files fixed: {fixed_count}")

# Also check and fix any other files
print("\n" + "="*80)
print("CHECKING ALL FILES IN src FOLDER")
print("="*80)

src_dir = "src"
all_fixed = 0

for root, dirs, files in os.walk(src_dir):
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            if fix_file_imports(filepath):
                print(f"✅ Fixed: {filepath}")
                all_fixed += 1

print(f"\nTotal all files fixed: {all_fixed}")
print("="*80)
print("DONE! Now run your tests again.")