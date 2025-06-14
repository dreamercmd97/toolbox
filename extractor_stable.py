def extractor(input_file, block_name, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(output_file, 'w', encoding='utf-8') as out:
        for line in lines:
            if line.strip().startswith(f'"{block_name}"'):
                formatted_line = '{' + line.strip().rstrip(',') + '}'
                out.write(formatted_line + '\n')

    print(f"{block_name} blokları '{output_file}' dosyasına yazıldı.")

# Kullanım
extractor("fxidmap_formatted.tsl", "PATCH%FX(1)", "PATCH_FX1_blocks.tsl")
