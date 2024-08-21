# masa
def elegir_masa():
    masas = ["Masa Tradicional", "Masa Delgada", "Masa con Bordes de Queso"]
    print("Tipos de masa disponibles:")
    for i, masa in enumerate(masas, 1):
        print(f"{i}. {masa}")
    eleccion = int(input("Elige el tipo de masa: "))
    return masas[eleccion - 1]

# salsa
def elegir_salsa():
    salsas = ["Salsa de Tomate", "Salsa Alfredo", "Salsa Barbecue", "Salsa Pesto"]
    print("Tipos de salsa disponibles:")
    for i, salsa in enumerate(salsas, 1):
        print(f"{i}. {salsa}")
    eleccion = int(input("Elige el tipo de salsa: "))
    return salsas[eleccion - 1]

# ingredientes.py
def agregar_ingredientes(ingredientes_actuales):
    ingredientes_disponibles = ["Tomate", "Champiñones", "Aceituna", "Cebolla", "Pollo", "Jamón", "Carne", "Tocino", "Queso"]
    
    print("Ingredientes disponibles:")
    for i, ingrediente in enumerate(ingredientes_disponibles, 1):
        print(f"{i}. {ingrediente}")
    
    eleccion = input("Elige los ingredientes a agregar (puedes seleccionar varios separándolos por comas): ")
    elecciones = [int(e.strip()) for e in eleccion.split(',')]
    
    for eleccion in elecciones:
        ingrediente_seleccionado = ingredientes_disponibles[eleccion - 1]
        if ingrediente_seleccionado not in ingredientes_actuales:
            ingredientes_actuales.append(ingrediente_seleccionado)
    
    return ingredientes_actuales


def eliminar_ingredientes(ingredientes_actuales):
    print("Ingredientes actuales:")
    for i, ingrediente in enumerate(ingredientes_actuales, 1):
        print(f"{i}. {ingrediente}")
    eleccion = int(input("Elige el ingrediente a eliminar: "))
    ingrediente_seleccionado = ingredientes_actuales[eleccion - 1]
    ingredientes_actuales.remove(ingrediente_seleccionado)
    return ingredientes_actuales

def mostrar_ingredientes(ingredientes_actuales):
    print("Ingredientes actuales en la pizza:")
    for ingrediente in ingredientes_actuales:
        print(f"- {ingrediente}")


# pedido
def confirmar_pedido(masa, salsa, ingredientes):
    tiempo_estimado = 20 + 2 * len(ingredientes)
    print(f"Tu pizza con {masa}, {salsa} y los siguientes ingredientes: {', '.join(ingredientes)} estará lista en {tiempo_estimado} minutos.")
    confirmacion = input("¿Deseas confirmar el pedido? (si/no): ")
    if confirmacion.lower() == "si":
        print("Pedido confirmado. ¡Gracias por tu compra!")
    else:
        print("Pedido cancelado.")