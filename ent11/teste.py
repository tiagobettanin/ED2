def criar_indices(nome_arquivo, coluna_chave_primaria=0, coluna_chave_secundaria=3):
    indice_primario = {}
    indice_secundario = {}
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()
        for rrn, linha in enumerate(linhas[1:]):
            campos = linha.strip().split(',')
            if len(campos) > max(coluna_chave_primaria, coluna_chave_secundaria):
                chave_primaria = campos[coluna_chave_primaria]
                chave_secundaria = campos[coluna_chave_secundaria]

                if chave_primaria not in indice_primario:
                    indice_primario[chave_primaria] = rrn + 1

                if chave_secundaria not in indice_secundario:
                    indice_secundario[chave_secundaria] = []
                indice_secundario[chave_secundaria].append(chave_primaria)

    return indice_primario, indice_secundario

def pesquisar_com_indice_secundario(chave_secundaria, indice_primario, indice_secundario, nome_arquivo):
    resultados = []
    if chave_secundaria in indice_secundario:
        chaves_primarias_encontradas = indice_secundario[chave_secundaria]
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            linhas = f.readlines()
            for chave_primaria in chaves_primarias_encontradas:
                if chave_primaria in indice_primario:
                    rrn = indice_primario[chave_primaria]
                    resultados.append(linhas[rrn].strip())
    return resultados

if __name__ == "__main__":
    nome_arquivo = "heroes_dataset.csv"

    indice_primario, indice_secundario = criar_indices(nome_arquivo, 0, 3)

    print("Índice Secundário (Alinhamento -> [Heróis]) criado.")
    for alinhamento, herois in list(indice_secundario.items())[:3]:
         print(f"  '{alinhamento}': {herois[:2]}...")
    print("-" * 30)

    chave_busca = input("Digite o alinhamento para buscar (ex: good, bad, neutral): ")
    registros_encontrados = pesquisar_com_indice_secundario(chave_busca, indice_primario, indice_secundario, nome_arquivo)

    if registros_encontrados:
        print(f"\nRegistros encontrados para o alinhamento '{chave_busca}':")
        for registro in registros_encontrados:
            print("  -", registro)
    else:
        print(f"Nenhum herói encontrado com o alinhamento '{chave_busca}'.")