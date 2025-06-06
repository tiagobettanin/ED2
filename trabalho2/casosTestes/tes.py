class Heroi:
    def __init__(self, key, name, alignment, gender, eye_color, race, hair_color, publisher,
                 skin_color, height, weight, intelligence, strength, speed, durability,
                 power, combat, total):
        self.key = int(key)
        self.name = name
        self.alignment = alignment
        self.gender = gender
        self.eye_color = eye_color
        self.race = race
        self.hair_color = hair_color
        self.publisher = publisher
        self.skin_color = skin_color
        self.height = float(height)  
        self.weight = int(weight)
        self.intelligence = int(intelligence)
        self.strength = int(strength)
        self.speed = int(speed)
        self.durability = int(durability)
        self.power = int(power)
        self.combat = int(combat)
        self.total = int(total)

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __str__(self):
        return '|'.join([
            str(self.key), self.name, self.alignment, self.gender, self.eye_color,
            self.race, self.hair_color, self.publisher, self.skin_color,
            str(self.height), str(self.weight), str(self.intelligence),
            str(self.strength), str(self.speed), str(self.durability),
            str(self.power), str(self.combat), str(self.total)
        ])

def quick_sort(arr, low, high, ascending=True):
    if low < high:
        pi = partition(arr, low, high, ascending)
        quick_sort(arr, low, pi - 1, ascending)
        quick_sort(arr, pi + 1, high, ascending)

def partition(arr, low, high, ascending):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if ascending:
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        else:
            if arr[j] > pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def heapify(arr, n, i, ascending=True):
    largest_or_smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if ascending:
        if left < n and arr[left] > arr[largest_or_smallest]:
            largest_or_smallest = left
        if right < n and arr[right] > arr[largest_or_smallest]:
            largest_or_smallest = right
    else:
        if left < n and arr[left] < arr[largest_or_smallest]:
            largest_or_smallest = left
        if right < n and arr[right] < arr[largest_or_smallest]:
            largest_or_smallest = right

    if largest_or_smallest != i:
        arr[i], arr[largest_or_smallest] = arr[largest_or_smallest], arr[i]
        heapify(arr, n, largest_or_smallest, ascending)

def heap_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n // 2 -1, -1, -1):
        heapify(arr, n, i, ascending)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, ascending)

def merge_sort(arr, ascending=True):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, ascending)
        merge_sort(right_half, ascending)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if ascending:
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
            else:
                if left_half[i] > right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def insertion_sort(arr, ascending=True):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        if ascending:
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
        else:
            while j >= 0 and arr[j] < key:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Uso: python programa.py arquivo_entrada arquivo_saida")
        sys.exit(1)

    arquivo_entrada = sys.argv[1]
    arquivo_saida = sys.argv[2]

    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
    except:
        print("Erro ao abrir o arquivo de entrada.")
        sys.exit(1)

    if len(linhas) < 3:
        print("Arquivo de entrada inválido ou vazio.")
        sys.exit(1)

    meta_sort = None
    meta_order = None

    try:
        for token in linhas[0].strip().split(','):
            if token.startswith('SORT='):
                meta_sort = token.split('=')[1]
            elif token.startswith('ORDER='):
                meta_order = token.split('=')[1]
    except:
        print("Erro ao ler metadados no cabeçalho.")
        sys.exit(1)

    if meta_sort not in ['Q', 'M', 'H', 'I'] or meta_order not in ['C', 'D']:
        print("Parâmetros SORT ou ORDER inválidos.")
        sys.exit(1)

    header_campos = linhas[1].strip()
    registros = linhas[2:]

    herois = []
    for linha in registros:
        campos = linha.strip().split('|')
        if len(campos) < 18:
            continue
        heroi = Heroi(*campos[:18])
        herois.append(heroi)

    ascending = (meta_order == 'C')

    if meta_sort == 'Q':
        quick_sort(herois, 0, len(herois)-1, ascending)
    elif meta_sort == 'H':
        heap_sort(herois, ascending)
    elif meta_sort == 'M':
        merge_sort(herois, ascending)
    elif meta_sort == 'I':
        insertion_sort(herois, ascending)
    else:
        print("Método de ordenação não implementado.")
        sys.exit(1)

    try:
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            #f.write(linhas[0])
            f.write(header_campos + '\n')
            for heroi in herois:
                f.write(str(heroi) + '\n')
    except:
        print("Erro ao abrir o arquivo de saída.")
        sys.exit(1)
