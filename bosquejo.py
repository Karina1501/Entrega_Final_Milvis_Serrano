import dataset
miBase = dataset.connect("sqlite:///base.db")
tabla = miBase["Productos"]

while True:
    print("\n======= Sistema de Administración de Productos =======\n")
    print("1. Listar productos")
    print("2. Agregar producto")
    print("3. Eliminar producto por Nombre")
    print("4. Eliminar producto por ID")
    print("5. Actualizar Nuevo producto")
    print("6. Buscar Todos los producto")
    print("7. Salir")
    opcion = input("Elija una opción (1-7): ")
    
    match opcion:

        case "1":
            print("\n==== LISTA DE PRODUCTOS ====\n")   
            for items in tabla:
                print(f'ID:{items["id"]} | Producto: {items["Nombre"]} | Precio: {items["Precio"]} | Categoria: {items["Categoria"]}')

                
        case "2":
            print("\n==== AGREGAR PRODUCTO ====\n")
            agregarProducto = input("\nIngrese Nombre del Producto: ").strip()
            agregarPrecio = float(input("\nIngrese el Precio del Producto: ").strip())
            agregarCategoria = input("\nIngrese la Categoria del Producto: ").strip()

            agregar = {"Nombre":agregarProducto,"Precio":agregarPrecio,"Categoria":agregarCategoria}

            tabla.insert(agregar)

                                       
        case "3":
            print("\n==== ELIMINAR PRODUCTO ====\n")
            removerNombre = input("\nIngrese el nombre del producto a eliminar: ").strip()
            
            tabla.delete(Nombre=removerNombre)
            
            print(f"\n{removerNombre} se ha eliminado exitosamente!\n")
         
        case "4":
            print("\n==== ELIMINAR PRODUCTO POR ID ====\n")
            borrarID = int(input("\nID de prod. a borrar: ").strip())
            tabla.delete(id=borrarID)
            
            print(f"\nEl producto cuyo ID es {borrarID} fue quitado con exito!!!\n")
               
        case "5":
            print("\n==== ACTUALIZAR PRODUCTO ====\n")
            idBuscar = int(input("\nID a actualizar: "))
            
            nombreActualizar = input("\nIngrese Nombre Nuevo del Producto: ")
            precioActualizar = float(input("\nIngrese Precio Nuevo del Producto: "))
            catActualizar = input("\nIngrese Nueva Categoria del Producto: ")
            
            actualizar = {"id":idBuscar,"Nombre":nombreActualizar, "Precio":precioActualizar,"Categoria":catActualizar}
            tabla.upsert(actualizar,["id"])
        
        case "6":
            print("\n==== BUSCAR TODOS LOS PRODUCTOS ====\n")
            buscarTodo = input("\nIngrese Producto a buscar: ")
            
            encontrados = tabla.find(Nombre=buscarTodo)
            
            for encontrado in encontrados:
                print(f'{encontrado["Nombre"]} Se encontró en ID: {encontrado["id"]}')

        case "7":
             print("\n=== Gracias por usar el sistema de administración de productos. Hasta la próxima! ===\n")
             break
            
            

            
