def imprimir_matriz(matriz):
    for fila in matriz:
        print(' '.join(map(str, fila)))
    print()

def mover_vacio(matriz, direccion):
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == 0:
                if direccion == "IZQUIERDA" and j > 0:
                    matriz[i][j], matriz[i][j - 1] = matriz[i][j - 1], matriz[i][j]
                    return True
                elif direccion == "DERECHA" and j < 2:
                    matriz[i][j], matriz[i][j + 1] = matriz[i][j + 1], matriz[i][j]
                    return True
                elif direccion == "ARRIBA" and i > 0:
                    matriz[i][j], matriz[i - 1][j] = matriz[i - 1][j], matriz[i][j]
                    return True
                elif direccion == "ABAJO" and i < 2:
                    matriz[i][j], matriz[i + 1][j] = matriz[i + 1][j], matriz[i][j]
                    return True
    return False

# Matriz inicial
matriz = [[7, 1, 2], [8, 0, 3], [6, 5, 4]]

while True:
    imprimir_matriz(matriz)
    
    if matriz == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
        print("¡Felicidades! Has resuelto el rompecabezas.")
        break

    direccion = input("Mueve el espacio vacío (IZQUIERDA, DERECHA, ARRIBA, ABAJO): ").upper()

    if direccion in ["IZQUIERDA", "DERECHA", "ARRIBA", "ABAJO"]:
        if mover_vacio(matriz, direccion):
            continue
        else:
            print("Inténtalo de nuevo.")
    else:
        print("Dirección no válida. Por favor, ingresa una dirección válida.")
