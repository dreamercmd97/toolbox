#!/Users/ozgun/Downloads/PY_TOOLS/.venv/bin/python
import csv
import json

# JSON verini burada tanımla
json_input = """
{"PATCH%FX_DETAIL(1)": ["01", "01", "32", "32", "32", "32", "32", "01", "32", "32", "32", "32", "32", "32", "00", "32", "32", "32", "32", "32", "00", "32", "32", "32", "32", "00", "32", "32", "0B", "32", "32", "14", "14", "14", "14", "14", "14", "14", "14", "14", "14", "14", "00", "14", "0D", "01", "14", "17", "01", "14", "14", "0E", "14", "00", "32", "32", "32", "32", "32", "32", "32", "00", "32", "32", "32", "32", "32", "32", "32", "00", "32", "32", "00", "01", "18", "32", "00", "00", "00", "00", "32", "01", "18", "32", "00", "00", "00", "00", "32", "32", "32", "01", "0C", "00", "00", "00", "00", "46", "07", "00", "00", "00", "00", "50", "00", "64", "18", "18", "18", "18", "18", "18", "18", "18", "18", "18", "18", "18", "18", "18", "18", "18", "18", "18", "18", "18", "18", "18", "18", "18", "01", "32", "32", "10", "32", "32", "32", "00", "46", "28", "37", "00", "00", "64", "00", "1F", "28", "52", "32", "00", "3C", "00", "46", "55", "41", "32", "55", "3C", "32", "46", "3C", "64", "00", "32", "32", "32", "00", "50", "2D", "32", "00", "32", "64", "64", "01", "00", "02", "32", "50", "64", "32", "64", "08", "44", "18", "18", "38", "24", "47", "3B", "15", "2A", "32", "32", "32", "32", "01", "32", "2D", "32", "32", "50", "64", "00", "64", "64", "00", "00", "32", "32", "00", "01", "09", "00", "32", "64", "32", "00", "32", "00", "64", "24", "32", "64", "00"]}
"""

# JSON formatına çevir
try:
    # Eğer direkt sadece iç veri gelirse {} ile sarmalayalım
    if not json_input.strip().startswith("{"):
        json_input = "{" + json_input + "}"
    parsed_data = json.loads(json_input)
except json.JSONDecodeError as e:
    print(f"Hatalı JSON formatı: {e}")
    exit(1)

# Tek bir key bekliyoruz, onu çekelim
key = list(parsed_data.keys())[0]
values = parsed_data[key]

# Değerin bir liste olup olmadığını kontrol et
if not isinstance(values, list):
    print("Hata: JSON içindeki değer bir liste olmalıdır.")
    exit(1)

# CSV’ye yaz
csv_filename = "transposed_numbered.csv"
with open(csv_filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Index", "Value"])
    for i, val in enumerate(values, start=1):
        writer.writerow([i, val])

print(f"\n✅ Dönüştürme tamamlandı. Kaydedilen dosya: {csv_filename}")
