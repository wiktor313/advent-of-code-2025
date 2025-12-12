import sys

# Zwiększamy limit rekurencji, by obsłużyć głębokie ścieżki
sys.setrecursionlimit(5000)

# Wczytywanie danych (zgodnie z Twoim formatem)
with open('Day11\\Resources\\Input.csv', 'r') as file:
    devices = {}
    for line in file:
        line = line.strip()
        if ': ' in line:
            key, rest = line.split(': ')
            devices[key] = rest.split()
        elif line: # Obsługa linii bez sąsiadów
            key = line.split(':')[0]
            devices[key] = []

# Pamięć podręczna dla wyników (memoizacja)
memo = {}

def count_path(current, target, devices):
    # Jeśli dotarliśmy do celu, mamy 1 ścieżkę
    if current == target:
        return 1
    
    # Sprawdzamy, czy już liczyliśmy ścieżki z tego miejsca do TEGO KONKRETNEGO celu
    if (current, target) in memo:
        return memo[(current, target)]
    
    total_paths = 0
    # Sumujemy ścieżki od sąsiadów
    for neighbor in devices.get(current, []):
        total_paths += count_path(neighbor, target, devices)
    
    # Zapamiętujemy wynik
    memo[(current, target)] = total_paths
    return total_paths

# Obliczamy dwie możliwe warianty trasy przez wymagane węzły:
# Wariant 1: svr -> dac -> fft -> out
path1 = (count_path('svr', 'dac', devices) * count_path('dac', 'fft', devices) * count_path('fft', 'out', devices))

# Wariant 2: svr -> fft -> dac -> out
path2 = (count_path('svr', 'fft', devices) * count_path('fft', 'dac', devices) * count_path('dac', 'out', devices))

# Wynikiem jest suma (jeden z wariantów wyniesie 0, bo graf jest skierowany)
answer = path1 + path2
print(f"Answer: {answer}")