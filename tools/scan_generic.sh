#!/usr/bin/env bash

TARGET="$1"

if [ -z "$TARGET" ]; then
  echo "Uso: $0 <url-alvo>"
  exit 1
fi

echo "[+] Verificando headers..."
curl -I "$TARGET"

echo "[+] Exemplo de enumeração (não executado automaticamente):"
echo "feroxbuster -u $TARGET -w /path/wordlist -x php,html,txt"
