import pandas as pd

# -------------------- MÉTODO 01 --------------------
def escritaMetodo01():
    with open("anime.csv", "r", encoding="utf-8") as f:
        linhas = f.readlines()
    
    maior_tamanho = max(len(l.strip()) for l in linhas)
    
    with open("metodo1.txt", "w", encoding="utf-8") as f_out:
        for linha in linhas:
            linha = linha.strip().replace(",", "|")
            faltando = maior_tamanho - len(linha)
            if faltando > 0:
                linha += "*" * faltando
            f_out.write(linha + "\n")

def leituraMetodo01():
    with open("metodo1.txt", "r", encoding="utf-8") as f:
        for linha in f:
            print(linha.strip())

# -------------------- MÉTODO 02 --------------------
def escritaMetodo02():
    with open("anime.csv", "r", encoding="utf-8") as f:
        linhas = f.readlines()

    campos = []
    for linha in linhas:
        campos += linha.strip().split(",")

    with open("metodo2.txt", "w", encoding="utf-8") as f_out:
        f_out.write("|".join(campos))

def leituraMetodo02(idRegistro):
    with open("metodo2.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()

    campos = conteudo.strip().split("|")
    inicio = idRegistro * 3  # cada registro tem 3 campos
    fim = inicio + 3
    registro = campos[inicio:fim]
    print("Registro:", registro)

# -------------------- MÉTODO 03 --------------------
def escritaMetodo03():
    with open("anime.csv", "r", encoding="utf-8") as f:
        linhas = f.readlines()

    with open("metodo3.txt", "w", encoding="utf-8") as f_out:
        for linha in linhas:
            linha = linha.strip().replace(",", "|")
            tamanho = len(linha)
            f_out.write(f"{str(tamanho).zfill(3)}{linha}|")

def leituraMetodo03():
    with open("metodo3.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()

    i = 0
    while i < len(conteudo):
        tamanho = int(conteudo[i:i+3])
        i += 3
        registro = conteudo[i:i+tamanho]
        print(registro.split("|"))
        i += tamanho + 1  # +1 por conta do | final

# -------------------- MÉTODO 04 --------------------
def escritaMetodo04():
    with open("anime.csv", "r", encoding="utf-8") as f:
        linhas = f.readlines()

    indices = []
    conteudo = ""
    pos = 0
    for linha in linhas:
        linha = linha.strip().replace(",", "|")
        conteudo += linha + "#"
        indices.append(str(pos).zfill(3))
        pos += len(linha) + 1  # +1 por causa do "#"

    with open("metodo4.txt", "w", encoding="utf-8") as f_out:
        f_out.write(conteudo)

    with open("indice.txt", "w", encoding="utf-8") as f_idx:
        f_idx.write("\n".join(indices))

def leituraMetodo04(idRegistro):
    with open("metodo4.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()
    with open("indice.txt", "r", encoding="utf-8") as f:
        indices = [int(l.strip()) for l in f.readlines()]

    inicio = indices[idRegistro]
    fim = indices[idRegistro + 1] if idRegistro + 1 < len(indices) else len(conteudo)
    registro = conteudo[inicio:fim].strip("#")
    print(registro.split("|"))

# -------------------- MAIN --------------------
if __name__ == "__main__":
    escritaMetodo01()
    leituraMetodo01()

    # escritaMetodo02()
    # leituraMetodo02(1)

    # escritaMetodo03()
    # leituraMetodo03()

    # escritaMetodo04()
    # leituraMetodo04(2)
