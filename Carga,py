import concurrent.futures

def simular_usuario():
    r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    return r.status_code

usuarios = 10  # Não coloque 1000 para não sobrecarregar

with concurrent.futures.ThreadPoolExecutor() as executor:
    resultados = list(executor.map(lambda _: simular_usuario(), range(usuarios)))

print(f"Usuários simultâneos testados: {len(resultados)}")
print(f"Todos com status 200: {all(r == 200 for r in resultados)}")
