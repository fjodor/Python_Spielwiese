def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Index des kleinsten Elements im unsortierten Teil finden
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Tauschen: kleinstes Element an Position i
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Beispiel
daten = [64, 25, 12, 22, 11]
print(selection_sort(daten))
