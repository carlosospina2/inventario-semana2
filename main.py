# Importamos las funciones. 
import funciones 

def ejecutar_menu(): 
    validador = True
    while  validador :
        print("\n1. Agregar | 2. Mostrar | 3. Estadísticas | 4. Salir") 
        opcion = input("Selecciona: ")

        if opcion == "1":
            funciones.agregar_producto()
        elif opcion == "2":
            funciones.mostrar_inventario() 
        elif opcion == "3":
            funciones.calcular_estadisticas()
        elif opcion == "4":
            validador = False
    
        else:
            print("Opción no válida.")

if __name__=="__main__":
    ejecutar_menu()