def removeRegistro (arquivo, chave):
    
    try:
        with open('./animes.csv', 'r', encoding='utf-8') as f:
            registros = f.readlines()
            for i, r in enumerate(registros):
                registro = r.split('|')
                if chave == registro[0]:
                    novoRegistro = '*|' + r[2:]
                    registro[i] = novoRegistro
        return registro
                    
    except FileNotFoundError as e:
        print("Arquivo não encontrado", e)
        exit(1)
    
    
if __name__ == '__main__':
    chave = 'Shugo Chara'  
    registro = removeRegistro('./animes.csv', chave)
    print(registro[1])
