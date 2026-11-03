#!/bin/bash
# pdf.html -> site/Adonias_Nigussie_Website_Portfolio.pdf (headless Chrome, kill guard: Chrome often hangs here)
cd "$(dirname "$0")"
python3 pdf.py || exit 1
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT="$PWD/site/Adonias_Nigussie_Website_Portfolio.pdf"
rm -f "$OUT"; prof=$(mktemp -d)
"$CHROME" --headless=new --disable-gpu --no-sandbox --user-data-dir="$prof" \
  --no-pdf-header-footer --virtual-time-budget=30000 \
  --print-to-pdf="$OUT" "file://$PWD/pdf.html" >/dev/null 2>&1 &
pid=$!; i=0
while kill -0 $pid 2>/dev/null && [ $i -lt 120 ]; do sleep 2; i=$((i+2)); [ -s "$OUT" ] && [ $i -gt 10 ] && break; done
kill -9 $pid 2>/dev/null; rm -rf "$prof"
ls -la "$OUT"
