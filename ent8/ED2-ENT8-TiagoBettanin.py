# Exercício 01: grep
def grep(arquivo, string):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            encontrou = False
            for linha in f:
                linha = linha.strip('\n')
                campos = linha.split(',')       
                if any(string.lower() in campo.lower() for campo in campos):
                    print(linha)
                    encontrou = True
        if not encontrou:
            print('Elemento não encontrado')
    except FileNotFoundError as e:
        print("Erro ao abrir o arquivo:", e)

# Exercício 02: readRecordByRRN
def grep_com_indices(arquivo, string):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            encontrou = False
            for i, linha in enumerate(f):
                linha = linha.strip('\n')
                campos = linha.split(',')
                if any(string.lower() in campo.lower() for campo in campos):
                    print(f"RRN {i}: {linha}")
                    encontrou = True
        if not encontrou:
            print('Elemento não encontrado')
    except FileNotFoundError as e:
        print("Erro ao abrir o arquivo:", e)

# Exercício 03: readRecordByRRN
def readRecordByRRN(arquivo, RRN, filler='*'):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            linhas = [linha.strip('\n') for linha in f]

        if RRN < 0 or RRN >= len(linhas):
            print('RRN fora do intervalo')
            return None

        max_tamanho = max(len(linha) for linha in linhas)

        registro = linhas[RRN]
        registro_preenchido = registro.ljust(max_tamanho, filler)
        print(registro_preenchido)
        return registro_preenchido

    except FileNotFoundError as e:
        print("Erro ao abrir o arquivo:", e)
        return None

#Main
if __name__ == "__main__":

    arquivo = 'animes.csv' 
    palavra = 'Naruto'
    rrn_desejado = 0  #exemplo

    print("\n=== Exercício 01 ===")
    grep(arquivo, palavra)

    print("\n=== Exercício 02 ===")
    grep_com_indices(arquivo, palavra)

    print("\n=== Exercício 03 ===")
    readRecordByRRN(arquivo, rrn_desejado)
