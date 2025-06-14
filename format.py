#!/Users/ozgun/Downloads/PY_TOOLS/.venv/bin/python

import re
import os

def format_tsl_one_line_blocks(raw_text):
    # Her PATCH% bloğunu yakala
    pattern = r'"PATCH%[^"]+"\s*:\s*\[[^\]]*\]'
    matches = re.findall(pattern, raw_text.replace("\n", ""))

    cleaned_blocks = []
    for match in matches:
        # Boşlukları ve fazla tırnakları normalize et
        key, value = match.split(":", 1)
        value = value.strip().replace('"', '"').replace(" ", "")
        formatted = f"{key.strip()}: {value}"
        cleaned_blocks.append(formatted)

    return "\n".join(cleaned_blocks)

def main():
    input_path = input("TSL dosyasının yolunu girin (örnek: patch_raw.tsl): ").strip()

    if not os.path.exists(input_path):
        print("❌ Dosya bulunamadı.")
        return

    file_stem = os.path.splitext(os.path.basename(input_path))[0]
    output_path = f"{file_stem}_formatted.tsl"

    with open(input_path, "r", encoding="utf-8") as f:
        raw = f.read()

    formatted = format_tsl_one_line_blocks(raw)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(formatted)

    print(f"\n✅ Her blok tek satır olacak şekilde yazıldı: {output_path}")

if __name__ == "__main__":
    main()
