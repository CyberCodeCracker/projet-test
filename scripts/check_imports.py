# check_import_chain.py
import os

files_to_check = [
    "src/pages/login_page.py",
    "src/pages/menu_page.py", 
    "src/pages/menu_details_page.py",
    "src/pages/categories_page.py",
    "src/pages/items_page.py",
    "src/pages/admin_clients_page.py",
    "src/pages/checkout_page.py",
    "src/utils/config.py",
    "src/utils/helpers.py"
]

print("Checking imported files for 'src.' imports...")
print("="*80)

for filepath in files_to_check:
    if os.path.exists(filepath):
        print(f"\n📄 {filepath}:")
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines[:30], 1):  # Check first 30 lines
                if 'import' in line and 'src.' in line:
                    print(f"  Line {i}: {line.rstrip()}")
    else:
        print(f"\n❌ {filepath} not found!")