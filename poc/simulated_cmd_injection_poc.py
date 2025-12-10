"""
PoC SIMULADA — Command Injection
Detecta padrões suspeitos, sem executar comandos.
"""

import re

def detect_injection(data):
    pattern = re.compile(r"[;&|`]")
    return bool(pattern.search(data))

inputs = [
    "example.com",
    "example.com; ls",
    "8.8.8.8 | whoami"
]

for i in inputs:
    print(i, "-> suspeito?", detect_injection(i))
