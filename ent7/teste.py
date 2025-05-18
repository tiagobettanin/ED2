import pandas as pd  # Biblioteca para manipulação de dados sugerida pelo professor


# --------------------MÉTODO 01--------------------
def escritaMetodo01():
    # Abre o arquivo CSV original com a lista de animes no modo leitura e codificação UTF-8
    with open("./animes.csv", "r", encoding="utf-8") as f:
        linhas = f.readlines()  # Lê todas as linhas do arquivo e armazena como uma lista de strings

    # Descobre o tamanho da maior linha (registro) para padronizar todos os registros com o mesmo tamanho
    # strip() remove espaços extras; len() mede o comprimento da linha; max() pega a maior delas
    maior_tamanho = max(len(l.strip()) for l in linhas)

    # Cria um novo arquivo chamado metodo1.txt no modo escrita
    with open("metodo1.txt", "w", encoding="utf-8") as f_out:
        for linha in linhas:
            linha = linha.strip().replace(",", "|")  # Remove espaços e substitui vírgulas por pipes (|)
            faltando = maior_tamanho - len(linha)   # Calcula quantos caracteres faltam para completar o tamanho padrão
            if faltando > 0:
                linha += "*" * faltando  # Preenche o restante com '*' para manter o tamanho fixo
            f_out.write(linha + "\n")    # Escreve a linha formatada no novo arquivo

def leituraMetodo01():
    # Lê o arquivo metodo1.txt e imprime todas as linhas no console
    with open("metodo1.txt", "r", encoding="utf-8") as f:
        for linha in f:
            print(linha.strip())  # Imprime a linha sem espaços extras

# --------------------MÉTODO 02--------------------
def escritaMetodo02():
    # Lê todas as linhas do arquivo CSV original
    with open("./animes.csv", "r", encoding="utf-8") as f:
        linhas = f.readlines()

    campos = []  # Lista que irá armazenar todos os campos (separados)
    for linha in linhas:
        campos += linha.strip().split(",")  # Divide cada linha em campos separados por vírgula e adiciona à lista

    # Escreve todos os campos separados por | em uma única linha no novo arquivo
    with open("metodo2.txt", "w", encoding="utf-8") as f_out:
        f_out.write("|".join(campos))

def leituraMetodo02(idRegistro):
    # Lê todo o conteúdo do arquivo metodo2.txt como uma única string
    with open("metodo2.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()

    campos = conteudo.strip().split("|")  # Separa todos os campos usando o | como delimitador
    inicio = idRegistro * 3  # Cada registro tem 3 campos (nome, link, imagem), então calcula o índice inicial
    fim = inicio + 3         # Índice final é o início + 3 campos
    registro = campos[inicio:fim]  # Extrai os campos referentes ao registro desejado
    print("Registro:", registro)

# --------------------MÉTODO 03--------------------
def escritaMetodo03():
    # Lê todas as linhas do CSV original
    with open("./animes.csv", "r", encoding="utf-8") as f:
        linhas = f.readlines()

    # Cria o arquivo metodo3.txt com tamanho do registro antes de cada linha
    with open("metodo3.txt", "w", encoding="utf-8") as f_out:
        for linha in linhas:
            linha = linha.strip().replace(",", "|")  # Remove espaços e substitui vírgulas por |
            tamanho = len(linha)  # Calcula o tamanho da linha
            f_out.write(f"{str(tamanho).zfill(3)}{linha}|")  # Escreve o tamanho (com 3 dígitos), a linha, e um | final

def leituraMetodo03():
    # Lê todo o conteúdo do arquivo metodo3.txt
    with open("metodo3.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()

    i = 0  # Índice inicial de leitura
    while i < len(conteudo):
        tamanho = int(conteudo[i:i+3])  # Lê os 3 primeiros caracteres como inteiro (tamanho do registro)
        i += 3  # Avança para o início do conteúdo do registro
        registro = conteudo[i:i+tamanho]  # Lê a string do tamanho especificado
        print(registro.split("|"))  # Divide os campos e imprime
        i += tamanho + 1  # Avança para o próximo registro (pula o | final também)

# --------------------MÉTODO 04--------------------
def escritaMetodo04():
    # Lê as linhas do CSV original
    with open("./animes.csv", "r", encoding="utf-8") as f:
        linhas = f.readlines()

    indices = []     # Lista para armazenar os índices de início de cada registro
    conteudo = ""    # Conteúdo concatenado de todos os registros
    pos = 0          # Posição atual no arquivo

    for linha in linhas:
        linha = linha.strip().replace(",", "|")  # Formata a linha
        conteudo += linha + "#"  # Adiciona a linha ao conteúdo e separa com '#'
        indices.append(str(pos).zfill(3))  # Salva a posição inicial do registro, com zeros à esquerda
        pos += len(linha) + 1  # Atualiza a posição (linha + caractere separador)

    # Salva o conteúdo no arquivo principal
    with open("metodo4.txt", "w", encoding="utf-8") as f_out:
        f_out.write(conteudo)

    # Salva os índices no arquivo auxiliar
    with open("indice.txt", "w", encoding="utf-8") as f_idx:
        f_idx.write("\n".join(indices))  # Cada índice em uma linha

def leituraMetodo04(idRegistro):
    # Lê o conteúdo principal e os índices do arquivo
    with open("metodo4.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()
    with open("indice.txt", "r", encoding="utf-8") as f:
        indices = [int(l.strip()) for l in f.readlines()]  # Converte os índices em inteiros

    inicio = indices[idRegistro]  # Posição inicial do registro
    # Se não for o último registro, pega o próximo índice como fim; caso contrário, vai até o fim do conteúdo
    fim = indices[idRegistro + 1] if idRegistro + 1 < len(indices) else len(conteudo)
    registro = conteudo[inicio:fim].strip("#")  # Pega o conteúdo e remove o separador final
    print(registro.split("|"))  # Exibe os campos

# --------------------MAIN--------------------
if __name__ == "__main__":
     
     

     escritaMetodo01()
     leituraMetodo01()

     escritaMetodo02()
     leituraMetodo02(1)

     escritaMetodo03()
     leituraMetodo03()

     escritaMetodo04()
     leituraMetodo04(2)
