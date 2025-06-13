def criar_indice(nome_arquivo):
    indice = []
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()
        for i, linha in enumerate(linhas[1:]):
            campos = linha.strip().split(",")
            if len(campos) > 0:
                chave = campos[0]
                indice.append((chave, i + 1))
    indice.sort(key=lambda x: x[0])
    return indice

def pesquisar(indice, chave, nome_arquivo):
    inicio = 0
    fim = len(indice) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        atual = indice[meio]
        if atual[0] == chave:
            with open(nome_arquivo, "r", encoding="utf-8") as f:
                linhas = f.readlines()
                return linhas[atual[1]].strip()
        elif chave < atual[0]:
            fim = meio - 1
        else:
            inicio = meio + 1
    return None

if __name__ == "__main__":
    nome_arquivo = "heroes_dataset.csv"
    indice = criar_indice(nome_arquivo)
    chave = input("Digite o nome do herói para buscar: ")
    resultado = pesquisar(indice, chave, nome_arquivo)
    if resultado:
        print("Registro encontrado:", resultado)
    else:
        print("Herói não encontrado.")
