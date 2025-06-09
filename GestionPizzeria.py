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
menu = """=== MENÚ DE LAS PIPSAS ===
1. Registrar nuevas pizzas 🍕
2. Ver catálogo de pizzas 🗒️ 🍕
3. Realizar un pedido 🗒️✍️
4. Ver pedidos realizados 🗒️ ✅
5. Salir del sistema 👋
========================="""

Lista_Pedidos = [] #Aquí se guardan los pedidos
Lista_Pizzas = ['Pepperoni', 'Champiñones', 'Napolitana', 'Hawaiana'] #Lista que guarda las pizzas 

Precios_Pizza = {  #Dicciónario que guarda los precios
                'Pepperoni': 6000,
                'Champiñones': 7000,
                'Napolitana': 8000,
                'Hawaiana': 9500
            }

while True:
    os.system('cls')
    print(menu)
    opc = input("\nIngrese una opción: ")
    os.system('cls')

    if opc == '1':
        #Validar nombre de la pizza
        while True:
            Nueva_Pizza = input("Ingrese el tipo de su Pizza: ").capitalize()
            if len(Nueva_Pizza)>=3 and Nueva_Pizza.isalpha():
                if Nueva_Pizza in Lista_Pizzas:
                    print("❎ Esa pizza ya está registrada.")
                break
            else:
                print("❎ Nombre inválido. Debe tener al menos 3 letras y solo letras.")
        while True:
            try:
                precio = int(input(f"Ingrese el precio para la pizza {Nueva_Pizza}: "))
                if precio >0:
                    break
                else:
                    print("❎ El precio debe ser mayor a 0.")
            except ValueError:
                print("❎ Error! Ingrese un precio valido para su pizza 'Solo números'")

        Lista_Pizzas.append(Nueva_Pizza)  #Guardar en la lista las pizzas
        Precios_Pizza[Nueva_Pizza] = precio   #Guardar en la lista el precio de la nueva pizza
        print(f"✅ Pizza {Nueva_Pizza} registrada con éxito por ${precio}.")  #Pizza registrada con éxito
    
    elif opc == '2':  #Catálogo de Pizzas
        print("🗒️ Catálogo de Pizzas:\n")
        if len(Lista_Pizzas) == 0:
            print("❎ No hay Pizzas registradas.")
        else:
            for i, pizza in enumerate(Lista_Pizzas, 1):
                precio = Precios_Pizza.get(pizza, 'Sin precio')
                print(f"{i}. {pizza} | ${precio}")

    elif opc == '3':  #Realizar pedido
        Pedido = input("Ingrese su nombre: ")
        print("\n🗒️ Catálogo de Pizzas Disponibles:")
        for i, pizza in enumerate(Lista_Pizzas, 1):
            print(f"{i}. {pizza}")
        Pizza_Elegida = input("\nIngrese el nombre de la pizza que desea ordenar: ").capitalize()
        
        if Pizza_Elegida in Lista_Pizzas: 
            while True:
                try:
                    Cant_Pizza = int(input("Ingrese la cantidad de pizzas que desea: "))
                    if Cant_Pizza >0:
                        break
                    else:
                        print("❎ Debe ingresar una canttidad válida.")
                except ValueError:
                    print("❎ Debe ingresar un número válido.")
            
            
            precio_unitario = Precios_Pizza.get(Pizza_Elegida, 0)
            total_pagar = precio_unitario * Cant_Pizza
            #Dicciónario que guarda los pedidos
            Pedido = {
                "cliente": Pedido,
                "pizza": Pizza_Elegida,
                "cantidad": Cant_Pizza,
                "total": total_pagar
            }
            Lista_Pedidos.append(Pedido)
            
            print(f"\n✅ {Pedido}, ordenado con exito {Cant_Pizza} pizza(s) de {Pizza_Elegida}. ¡Gracias por su pedido!")
            print(f"💰 Total a pagar: ${total_pagar}")
        else:
            print("❎ Esa pizza no está en el catálogo.")
    
    elif opc == '4':  #Ver pedidos realizados
        print("🗒️✍️ Pedidos realizados:\n")
        if not Lista_Pedidos:
            print("❎ No hay pedidos registrados.")
        else:
            for i, p in enumerate(Lista_Pedidos, 1):
                print(f"{i}. |Cliente: {p['cliente']} | Pizza: {p['pizza']} | Cantidad: {p['cantidad']} | Total: ${p['total']}")

    elif opc == '5':  #Salir del menú
        print("Gracias por usar el Sistema de Gestion de Pizzas🍕. Adios! 👋")
        break
    else:
        print("   ❎  Opción incorrecta!  (Elige 1, 2, 3, 4, o 5)   ")
    print("\n...presione una tecla para continuar...")
    msvcrt.getch() 