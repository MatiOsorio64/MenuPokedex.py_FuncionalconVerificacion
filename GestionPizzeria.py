#   Crear Sistema de Gestión de Pedidos para una Pizzeria.
#	Registrar nuevas pizzas disponibles para la venta. 
#	Ver el catálogo de pizzas. 
#	Realizar un pedido, ingresando nombre del cliente, pizza seleccionada y cantidad. 
#	Ver los pedidos realizados. 
#	Salir del sistema. 

import os,time,msvcrt
#Mensaje de bienvenida
os.system('cls')
print("Bienvenido al Sistema de Gestión de la Pizzeria 🍕")
print("\npresione una tecla para continuar...")
msvcrt.getch() 
#MENÚ
menu = """        --- MENÚ --- 
1. Registrar nuevas pizzas 🍕
2. Ver catálogo de pizzas 🗒️🍕
3. Realizar un pedido 🗒️✍️
4. Ver pedidos realizados 🗒️✅
5. Salir del sistema 👋"""

ListaPizzas = ['Pepperoni', 'Champiñones', 'Napolitana', 'Hawaiana'] #Lista que guarda las pizzas 
while True:
    os.system('cls')
    print(menu)
    opc = input("\nIngrese una opción: ")
    os.system('cls')

    if opc == '1':
        #Validar nombre de la pizza
        while True:
            TipoPizza = input("Ingrese el tipo de su Pizza: ").capitalize()
            if len(TipoPizza)>=3:
                break
            else:
                print("❎ Nombre inválido. Debe tener al menos 3 letras y solo letras.")

        ListaPizzas.append(TipoPizza) #Guardar en la lista las pizzas
        print("✅ Pizza Guardada con éxito!")
    
    elif opc == '2':  #Catálogo de Pizzas
        print("🗒️ Catálogo de Pizzas:\n")
        if len(ListaPizzas) == 0:
            print("❎ No hay pizzas registradas.")
        else:
            for i, pizza in enumerate(ListaPizzas, 1):
                print(f"{i}. {pizza}")

    elif opc == '3':
        pass

    elif opc == '4':
        pass

    elif opc == '5':
        print("Gracias, Adios! 👋")
        break
    else:
        print("   ❎  Opción incorrecta!  (Elige 1, 2, 3, 4, o 5)   ")
    print("\n...presione una tecla para continuar...")
    msvcrt.getch() 