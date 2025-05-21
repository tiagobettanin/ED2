import sys
import random
import timeit

# Gera um vetor com base no tipo: crescente (c), decrescente (d) ou aleatório (r)
def gerar_vetor(tamanho, tipo):
    if tipo == 'c':
        return list(range(1, tamanho + 1))
    elif tipo == 'd':
        return list(range(tamanho, 0, -1))
    elif tipo == 'r':
        return [random.randint(0, 32000) for _ in range(tamanho)]

# Algoritmo Insertion Sort
def insertion_sort(v):
    comparacoes = 0
    for i in range(1, len(v)):
        chave = v[i]
        j = i - 1
        while j >= 0 and v[j] > chave:
            v[j + 1] = v[j]
            j -= 1
            comparacoes += 1
        if j >= 0:
            comparacoes += 1
        v[j + 1] = chave
    return v, comparacoes

# Algoritmo Selection Sort
def selection_sort(v):
    comparacoes = 0
    for i in range(len(v)):
        min_idx = i
        for j in range(i + 1, len(v)):
            comparacoes += 1
            if v[j] < v[min_idx]:
                min_idx = j
        v[i], v[min_idx] = v[min_idx], v[i]
    return v, comparacoes

# Algoritmo Bubble Sort
def bubble_sort(v):
    comparacoes = 0
    for i in range(len(v)):
        for j in range(0, len(v) - i - 1):
            comparacoes += 1
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
    return v, comparacoes

# Aplica um algoritmo de ordenação, mede tempo e grava resultado
def aplicar_algoritmo(nome, funcao, vetor_original, arquivo_saida):
    vetor_copia = vetor_original[:] # Copia para não alterar o original
    tempo = timeit.timeit(lambda: funcao(vetor_copia), number=1)
    resultado, comparacoes = funcao(vetor_copia)
    arquivo_saida.write(f"{nome} | {resultado} | Comparações: {comparacoes} | Tempo(ms): {tempo * 1000:.2f}\n")

# Função principal
def main():
    # Verifica se os dois arquivos (entrada e saída) foram informados
    
    #if len(sys.argv) != 3:
     #   print("Uso correto: python programa.py entrada.txt saida.txt")
     #   return

    # Lê os nomes dos arquivos da linha de comando
    #arquivo_entrada = sys.argv[1]
    #arquivo_saida = sys.argv[2]
    
    arquivo_entrada = 'input1.txt'
    arquivo_saida = 'output1.txt'
    
    import os
    print("Diretório atual:", os.getcwd())

    try:
        # Lê o tamanho do vetor e o tipo de geração ('c', 'd' ou 'r')
        with open('./input1.txt', 'r') as entrada:
            linhas = entrada.readlines()
            tamanho = int(linhas[0])
            tipo_vetor = linhas[1].strip()
            vetor = gerar_vetor(tamanho, tipo_vetor)
    except:
        print("Erro ao ler o arquivo de entrada. Verifique o formato e os dados.")
        return

    try:
        # Executa e grava os resultados de cada algoritmo no arquivo de saída
        with open(arquivo_saida, 'w') as saida:
            aplicar_algoritmo("InsertionSort", insertion_sort, vetor, saida)
            aplicar_algoritmo("SelectionSort", selection_sort, vetor, saida)
            aplicar_algoritmo("BubbleSort", bubble_sort, vetor, saida)
            # Você pode adicionar mais algoritmos aqui, se quiser
    except:
        print("Erro ao escrever no arquivo de saída.")

# Executa o programa
if __name__ == "__main__":
    main()