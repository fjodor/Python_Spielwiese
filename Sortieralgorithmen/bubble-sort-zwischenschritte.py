def bubble_sort_debug(arr):
    n = len(arr)
    print("Ausgangsliste:", arr)
    print("-" * 40)

    for i in range(n):
        print(f"Runde {i + 1}:")
        tausche_in_runde = False

        for j in range(0, n - i - 1):
            print(f"  Vergleiche arr[{j}] = {arr[j]} mit arr[{j+1}] = {arr[j+1]}")

            if arr[j] > arr[j + 1]:
                print(f"    → Tausche {arr[j]} und {arr[j+1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                tausche_in_runde = True
            else:
                print("    → Kein Tausch")

        print("  Ergebnis nach Runde:", arr)
        print("-" * 40)

        # Wenn keine Tausche mehr stattfinden, ist die Liste bereits sortiert
        if not tausche_in_runde:
            print("Keine Tausche mehr – Liste ist sortiert.")
            break

    return arr


# Beispielaufruf
daten = [64, 34, 25, 12, 22, 11, 90]
sortiert = bubble_sort_debug(daten)
print("Finale sortierte Liste:", sortiert)