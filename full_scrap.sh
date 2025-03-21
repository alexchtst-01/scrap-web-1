#!/bin/bash

# Berhenti jika ada error
set -e

# Array of URLs
url_targets=(
    "https://lpse.lkpp.go.id/eproc4/lelang?kategoriId=&tahun=2014"
    "https://lpse.lkpp.go.id/eproc4/lelang?kategoriId=&tahun=2015"
)

source .venv/Scripts/activate


# Loop melalui setiap URL dalam array
for url in "${url_targets[@]}"; do
    echo "Scraping data from: $url"
    python main.py -url="$url"
done

echo "All URLs processed!"
