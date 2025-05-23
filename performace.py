import timeit

# Código que queremos medir o desempenho
def codigo_teste():
  soma = 0
  for i in range (900000):
    soma += 1
  return soma

# Medindo o tempo de execução
tempo_execucao = timeit.timeit(codigo_teste, number=1)
print(f"Tempo de Execução: {tempo_execucao:.4f} segundos")

Saida: Tempo de Execução: 0.0393 segundos
