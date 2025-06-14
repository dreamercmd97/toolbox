#!/Users/oz/Downloads/PY_TOOLS/toolbox/.venv/bin/python

import sys
import re

def set_block_key(new_value):
    with open("search_param.py", "r", encoding="utf-8") as f:
        content = f.read()

    # BLOCK_KEY satırını bul ve değiştir
    new_content = re.sub(
        r'BLOCK_KEY\s*=\s*".*?"',
        f'BLOCK_KEY = "{new_value}"',
        content
    )

    with open("search_param.py", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "block":
        value = sys.argv[2].strip('"')
        set_block_key(value)
        print(f"BLOCK_KEY güncellendi: {value}")
    else:
        print('Kullanım: python define.py block "PATCH%FX(1)"')
