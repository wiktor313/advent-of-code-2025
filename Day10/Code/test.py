import numpy as np

# https://adventofcode.com/2025/day/10#part2

def solve_linear_system(target, buttons_indices):
    """
    Rozwiązuje problem jako układ równań Ax = B.
    A - macierz przycisków (kolumny to przyciski, wiersze to indeksy w target)
    x - wektor liczby naciśnięć (szukane)
    B - wektor docelowy (target)
    """
    n_equations = len(target) # Liczba wymiarów (wiersze)
    n_vars = len(buttons_indices) # Liczba przycisków (kolumny)
    
    # Jeśli liczba przycisków nie jest równa liczbie wymiarów, 
    # proste odwracanie macierzy (solve) może nie zadziałać.
    # W zadaniach AoC zazwyczaj jest to macierz kwadratowa.
    if n_equations != n_vars:
        return -1 

    # Budowanie macierzy A
    # A[i][j] = 1 jeśli przycisk j zwiększa wartość na indeksie i
    A = np.zeros((n_equations, n_vars), dtype=int)
    
    for btn_idx, indices_affected in enumerate(buttons_indices):
        for row_idx in indices_affected:
            A[row_idx, btn_idx] = 1
            
    B = np.array(target, dtype=np.float64)
    
    try:
        # Rozwiązujemy układ równań Ax = B
        x = np.linalg.solve(A, B)
        
        # Numeryczne zaokrąglanie (ponieważ solve operuje na floatach)
        x_rounded = np.round(x).astype(np.int64)
        
        # Weryfikacja rozwiązania:
        # 1. Czy liczby są całkowite (różnica między float a round znikoma)?
        # 2. Czy liczby są nieujemne (nie można nacisnąć przycisku -5 razy)?
        # 3. Czy rozwiązanie jest dokładne matematycznie?
        
        is_integer = np.allclose(x, x_rounded, atol=1e-3, rtol=0)
        is_positive = np.all(x_rounded >= 0)
        
        if is_integer and is_positive:
            # Sprawdzenie ostateczne (uniknięcie błędów precyzji przy ogromnych liczbach)
            # Mnożenie macierzy z powrotem musi dać target
             if np.array_equal(A @ x_rounded, np.array(target, dtype=np.int64)):
                return np.sum(x_rounded)
                
        return -1

    except np.linalg.LinAlgError:
        # Macierz osobliwa (brak rozwiązania lub nieskończenie wiele rozwiązań)
        return -1

# --- Wczytywanie danych (bez zmian) ---
#with open('Day10\\Resources\\Input.csv', 'r') as file:
with open('Day10\\Resources\\Sample.csv', 'r') as file:
    targets = []
    all_buttons = []
    
    for line in file:
        if not line.strip(): continue
        
        try:
            button_str = line.split(']', 1)[1].split('{', 1)[0].strip()
            buttons = []
            # Parsowanie przycisków (indeksów, które inkrementują)
            parts = button_str.split('(')[1:]
            for part in parts:
                numbers_str = part.split(')')[0]
                if numbers_str:
                    numbers = [int(x) for x in numbers_str.split(',')]
                    buttons.append(numbers)
            all_buttons.append(buttons)
            
            target_str = line.split('{')[1].split('}')[0]
            target = [int(x) for x in target_str.split(',')]
            targets.append(target)
        except IndexError:
            continue

# --- Obliczenia ---
answer = 0
for idx, (target, buttons) in enumerate(zip(targets, all_buttons)):
    # Używamy metody algebraicznej zamiast A*
    min_presses = solve_linear_system(target, buttons)
    
    if min_presses != -1:
        answer += min_presses

print(f"Answer: {answer}")