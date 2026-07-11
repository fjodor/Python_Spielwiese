def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        tausche_in_runde = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                tausche_in_runde = True

        # Wenn keine Tausche mehr stattfinden, ist die Liste bereits sortiert
        if not tausche_in_runde:
            break

    return arr

# Beispielaufruf
daten = [64, 34, 25, 12, 22, 11, 90]
sortiert = bubble_sort(daten)
print("Sortierte Liste:", sortiert)