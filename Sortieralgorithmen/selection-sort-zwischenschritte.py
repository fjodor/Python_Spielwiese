def selection_sort_debug(arr):
    n = len(arr)
    print(f"Start: {arr}")

    for i in range(n):
        min_index = i
        print(f"\n--- Durchlauf {i+1} ---")
        print(f"Suche Minimum im Bereich arr[{i}:{n}]")

        # Minimum im unsortierten Bereich finden
        for j in range(i + 1, n):
            print(f"Vergleiche arr[{j}] = {arr[j]} mit aktuellem Minimum arr[{min_index}] = {arr[min_index]}")
            if arr[j] < arr[min_index]:
                min_index = j
                print(f"→ Neues Minimum gefunden: arr[{min_index}] = {arr[min_index]}")

        # Tauschen
        print(f"Tausche arr[{i}] = {arr[i]} mit arr[{min_index}] = {arr[min_index]}")
        arr[i], arr[min_index] = arr[min_index], arr[i]

        print(f"Liste nach Durchlauf {i+1}: {arr}")

    print(f"\nFertig sortiert: {arr}")
    return arr


# Beispiel
daten = [64, 25, 12, 22, 11]
selection_sort_debug(daten)
