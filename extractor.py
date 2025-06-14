#!/Users/oz/Downloads/PY_TOOLS/toolbox/.venv/bin/python
import sys
import os
import re
import json
import os

# Bulunduğun klasörü path'e ekle
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Test etmek için path'leri bastıralım
print("PYTHON PATH:", sys.path)

# Şimdi import etmeyi dene
from search_param import BLOCK_KEY # type: ignore

print("BLOCK_KEY:", BLOCK_KEY)


def extract_block_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if BLOCK_KEY in line:
                try:
                    # Regex ile PATCH%FX(1) bloğunu ayıkla: örn. "PATCH%FX(1)": ["17"]
                    #match = re.search(r'"PATCH%FX\(1\)"\s*:\s*\[[^\]]*\]', line)
                    match = re.search(rf'"{re.escape(BLOCK_KEY)}"\s*:\s*\[[^\]]*\]', line)
                    if match:
                        block_line = "{" + match.group(0) + "}"
                        json_obj = json.loads(block_line)
                        json.dump(json_obj, outfile)
                        outfile.write("\n")
                except Exception as e:
                    print(f"Hata: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Kullanım: python3 extractor.py <dosya_adı.tsl>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = os.path.splitext(input_filename)[0] + "_ext_block.tsl"

    extract_block_lines(input_filename, output_filename)
    print(f"Bitti. Çıktı dosyası: {output_filename}")
