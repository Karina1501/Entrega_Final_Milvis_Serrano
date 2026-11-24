import json
productos = [] 

try:
    with open("datos.json","r") as archivo:
        productos = json.load(archivo)

except FileNotFoundError:
    with open("datos.json","w") as archivo:
        productos = []
        
        
def sincronizar():
    with open("datos.json","w") as archivo:
        json.dump(productos,archivo)  

while True:
        print("\n======= Sistema de Administración de Productos =======\n")
        print("1. Listar productos")
        print("2. Agregar producto")
        print("3. Eliminar producto")
        print("4. Buscar producto")
        print("5. Salir")
        opcion = input("Elija una opción (1-5): ")

        if opcion == "1":
            if not productos:
                print(" El inventario está vacío.")
            else:
                print("\n==== LISTA DE PRODUCTOS ====\n")
                for producto in productos:
                    print(f"Producto: {producto[1]} | Precio: $ {producto[2]} | Categoria: {producto[0]} | Stock: {producto[3]}")
            
        elif opcion == "2":
            print("\n==== AGREGAR PRODUCTOS ====\n")
            categoria = input("Ingrese la Categoria del producto: ").strip().lower()
            nombre = input("Ingrese nombre del producto: ").strip().lower()
            try:
                precio = float(input("Ingrese precio del producto: "))
                stock = int(input("Ingrese stock inicial: "))
                agregar = (categoria, nombre, precio, stock)
                productos.append(agregar)
                sincronizar()
            except ValueError:
                print(" Entrada inválida. El precio y el stock deben ser números.")
        
        elif opcion == "3":
             print("\n==== ELIMINAR PRODUCTOS ====\n")
             eliminar = input("\nIngrese el nombre del producto a eliminar: \n").strip().lower()
             if eliminar in productos:
                productos.remove(eliminar)
                print(f"\nSe ha eliminado {eliminar} exitosamente.\n")
             else:
                  print(f"\nNo se encontró {eliminar} en la lista de productos.\n") 
        
        elif opcion == "4":
            print("\n==== BUSCAR PRODUCTOS ====\n")
            buscar = input("\nIngrese el nombre del producto a buscar: \n").strip().lower()
            if buscar in productos:
                print(f"\nSe encontraron resultados de {buscar} con éxito.\n")
            else:
                print(f"\nNo se encontraron resultados de {buscar} en la búsqueda.\n")
           
        elif opcion == "5":
            print("\n*** Gracias por usar el sistema de administración de productos. Hasta la próxima! ***\n")
            break
        else:
            print("\n*** Opción inválida. Por favor, seleccione una opción válida del menú. ***\n")