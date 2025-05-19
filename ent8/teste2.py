# Exercício 01: grep - retorna registros que contêm a string
def grep(string):
    registros_encontrados = set()
    try:
        with open('./animes.csv', 'r', encoding='utf-8') as f:
            for linha in f:
                linha = linha.strip('\n')
                campos = linha.split(',')
                if string in campos:
                    registros_encontrados.add(linha)
    except FileNotFoundError as e:
        print("Arquivo não encontrado", e)
        exit(1)

    if not registros_encontrados:
        return 'Elemento não encontrado'
    else:
        return registros_encontrados


# Exercício 02: grep_com_indices - retorna registros e RRN (índice da linha)
def grep_com_indices(string):
    resultado = []
    try:
        with open('./animes.csv', 'r', encoding='utf-8') as f:
            for i, linha in enumerate(f):
                linha = linha.strip('\n')
                campos = linha.split(',')
                if string in campos:
                    resultado.append((i, linha))  # RRN, Registro
    except FileNotFoundError:
        print("Arquivo não encontrado")
        exit(1)

    if not resultado:
        return 'Elemento não encontrado'
    else:
        return resultado


# Exercício 03: readRecordByRRN - retorna o registro de RRN fixando o tamanho
def readRecordByRRN(RRN, filler='*'):
    try:
        with open('./animes.csv', 'r', encoding='utf-8') as f:
            linhas = [linha.strip('\n') for linha in f]

        if RRN < 0 or RRN >= len(linhas):
            return 'RRN fora do intervalo'

        # Descobre o tamanho do maior registro
        max_tamanho = max(len(linha) for linha in linhas)

        # Retorna o registro desejado preenchido com o caractere especial
        registro = linhas[RRN]
        registro_preenchido = registro.ljust(max_tamanho, filler)
        return registro_preenchido

    except FileNotFoundError:
        print("Arquivo não encontrado")
        exit(1)


# ==============================
# Exemplo de uso dos exercícios
# ==============================

palavra = 'Naruto'          # string de busca
rrn_desejado = 2            # RRN para teste

# Teste do Exercício 01

import os
print("Diretório atual:", os.getcwd())

print("\n=== Exercício 01 ===")
res1 = grep(palavra)
if isinstance(res1, str):
    print(res1)
else:
    for registro in res1:
        print(registro)

# Teste do Exercício 02
print("\n=== Exercício 02 ===")
res2 = grep_com_indices(palavra)
if isinstance(res2, str):
    print(res2)
else:
    for idx, registro in res2:
        print(f"RRN {idx}: {registro}")

# Teste do Exercício 03
print("\n=== Exercício 03 ===")
registro_rrn = readRecordByRRN(rrn_desejado)
print(f"Registro com RRN {rrn_desejado}: {registro_rrn}")
