import sys

class Heroi:
    def __init__(self, key, name, alignment, gender, eye_color, race, hair_color,
                 publisher, skin_color, height, weight,
                 intelligence, strength, speed, durability, power, combat, total):
        self.key = key
        self.name = name
        self.alignment = alignment
        self.gender = gender
        self.eye_color = eye_color
        self.race = race
        self.hair_color = hair_color
        self.publisher = publisher
        self.skin_color = skin_color
        self.height = height
        self.weight = weight
        self.intelligence = int(intelligence)
        self.strength = int(strength)
        self.speed = int(speed)
        self.durability = int(durability)
        self.power = int(power)
        self.combat = int(combat)
        self.total = int(total)

    def __str__(self):
        return f"{self.key}|{self.name}|{self.alignment}|{self.gender}|{self.eye_color}|{self.race}|" \
               f"{self.hair_color}|{self.publisher}|{self.skin_color}|{self.height}|{self.weight}|" \
               f"{self.intelligence}|{self.strength}|{self.speed}|{self.durability}|{self.power}|" \
               f"{self.combat}|{self.total}"

def quicksort_herois(herois, reverse=False):
    if len(herois) <= 1:
        return herois
    pivo = herois[0]
    menores = [h for h in herois[1:] if h.total < pivo.total]
    maiores = [h for h in herois[1:] if h.total >= pivo.total]
    resultado = quicksort_herois(menores, reverse) + [pivo] + quicksort_herois(maiores, reverse)
    return resultado[::-1] if reverse else resultado

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python keysorting.py entrada.txt saida.txt")
        sys.exit(1)

    entrada = sys.argv[1]
    saida = sys.argv[2]

    try:
        with open(entrada, 'r', encoding='utf-8') as f:
            linhas = [linha.strip() for linha in f if linha.strip()]
    except:
        print("Erro ao abrir o arquivo de entrada.")
        sys.exit(1)

    if len(linhas) < 3:
        print("Arquivo com dados insuficientes.")
        sys.exit(1)

    sort_line = linhas[0]
    order_line = linhas[1]
    cabecalho = linhas[2]
    dados = linhas[3:]

    if 'SORT=Q' not in sort_line or ('ORDER=C' not in order_line and 'ORDER=D' not in order_line):
        print("Parâmetros inválidos. Use SORT=Q e ORDER=C ou ORDER=D.")
        sys.exit(1)

    reverse = 'ORDER=D' in order_line

    herois = []
    for linha in dados:
        campos = linha.split('|')
        if len(campos) != 18:
            continue  # Ignora linhas com erro
        heroi = Heroi(*campos)
        herois.append(heroi)

    herois_ordenados = quicksort_herois(herois, reverse)

    try:
        with open(saida, 'w', encoding='utf-8') as f:
            f.write(cabecalho + '\n')
            for h in herois_ordenados:
                f.write(str(h) + '\n')
    except:
        print("Erro ao salvar o arquivo de saída.")
        sys.exit(1)
