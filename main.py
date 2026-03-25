# We import the functions.. 
import functions

print ("   ¡¡WELCOME STORE!!"    )  

def run_menu(): 
   validator= True
   while  validator :
        print("\n1. Add | 2. Sample | 3. Statistics | 4. go out") 
        opcion = input("Select: ")

        if opcion == "1":
            functions.add_product()
        elif opcion == "2":
            functions.show_inventory() 
        elif opcion == "3":
            functions.calculate_statistics()
        elif opcion == "4":
            validator = False
    
        else:
            print("Invalid option.")

if __name__=="__main__":
    run_menu()

