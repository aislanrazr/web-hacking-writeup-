"""
PoC SIMULADA – SQL Injection
Demonstra como entradas maliciosas podem afetar consultas,
mas **não executa** nenhuma interação com banco real.
"""

def simulate_query(user, password):
    query = f"SELECT * FROM users WHERE user='{user}' AND pass='{password}'"
    print("[DEBUG] Consulta simulada:", query)

tests = [
    ("admin", "123"),
    ("admin'--", "x"),
    ("' OR '1'='1", "' OR '1'='1")
]

for u, p in tests:
    simulate_query(u, p)
