import re

def parse_lines(file_path):
    with open(file_path, "r") as f:
        for line in f:
            if "200" in line or "301" in line:
                print("Found path:", line.strip())

# Exemplo de uso:
# parse_lines("resultado.txt")
