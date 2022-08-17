#pila
class Pila:
    def __init__(self, tamaño):
        self.pilas = []
        self.tamaño = tamaño
        
    def size(self):
        if len(self.pilas) > self.tamaño:
            print(f"No se pueden añadir mas valores, el tamaño establecido de valores en pila es: {self.tamaño}")
            exit()


    def push(self):
        valor = input("Ingrese valor a la pila:")
        self.pilas.append(valor)

    def pop(self):
        if self.longitud():
            return None
        else:
            self.pilas.pop() 

    def longitud(self):
        if len(self.pilas) == 0:
            return True
        else:
            return False

    def Eliminar(self):
        dato, value = self.buscar()
        if value == True:
            self.pilas.pop(self.pilas.index(dato))
            print(f"{dato} ha sido eliminado de Pila = {self.pilas}")
        else:
            print(f"{dato} no ha sido eliminado de Pila porque no se encuentra= {self.pilas}")

    def Insertar(self):
        dato = input("Ingresa el dato que quieres añadir a la pila:")
        posicion = int(input("Ingresa la posicion donde quieres colocar el elemento:"))
        self.pilas.insert(posicion -1, dato)

    def show(self):
        print(self.pilas)

    def buscar(self):
        dato = input("Ingresa el dato que quieres buscar:")
        if dato in self.pilas:
            print(f"{dato} esta en la pila {self.pilas}")
            return dato, True
        else:
            print(f"{dato} no se encuentra en la pila{self.pilas}")
            return dato, False

    def pila(self, option2):
        # Inicializar pila
        if option2 == 1:
            self.push()
        elif option2 == 2:
            self.pop()
        elif option2 == 3:
            self.show()
        # Ver si se trata de eliminar un elemento en la pila o cola por la entrada de dato 
        elif option2 == 4:
            self.Eliminar()
        #  Ver si se trata de agregar un elemento en la pila o cola por la entrada de dato 
        elif option2 == 5:
            self.Insertar()
        elif option2 == 6:
            self.buscar()
        elif option2 == 7:
            print ("La seción ha finalizado")
            exit()

#cola
class Cola:
    def __init__(self, tamaño):
        self.colas = []
        self.tamaño = tamaño

    def size(self):
        if len(self.colas) > self.tamaño:
            print(f"No se pueden añadir mas valores, el tamaño establecido de valores en cola es: {self.tamaño}")
            exit()

    

    def push(self):
        valor = input("Ingrese valor a la cola:")
        self.colas.append(valor)

    def pop(self):
        if self.longitud():
            return None
        else:
            self.colas.pop(0) 

    def longitud(self):
        if len(self.colas) == 0:
            return True
        else:
            return False

    def Eliminar(self):
        dato, value = self.buscar()
        if value == True:
            self.colas.pop(self.colas.index(dato))
            print(f"{dato} ha sido eliminado de Cola = {self.colas}")
        else:
            print(f"{dato} no ha sido eliminado de Cola porque no se encuentra= {self.colas}")

    def Insertar(self):
        dato = input("Ingresa el dato que quieres añadir a la cola:")
        posicion = int(input("Ingresa la posicion donde quieres colocar el elemento:"))
        self.colas.insert(posicion -1, dato)

    def show(self):
        print(self.colas)

    def buscar(self):
        dato = input("Ingresa el dato que quieres buscar:")
        if dato in self.colas:
            print(f"{dato} esta en la cola {self.colas}")
            return dato, True
        else:
            print(f"{dato} no esta en la cola {self.colas}")
            return dato, False

    def cola(self, option2):
        # Inicializar pila
        if option2 == 1:
            self.push()
        elif option2 == 2:
            self.pop()
        elif option2 == 3:
            self.show()
        elif option2 == 4:
            self.Eliminar()
        elif option2 == 5:
            self.Insertar()
        elif option2 == 6:
            self.buscar()
        elif option2 == 7:
            print ("La seción ha finalizado")
            exit()
  
def process(option):
    if option == 1:
        print(submenu())
        print()
        option2 = int(input("Ingresa una opcion [1] al [7]:"))
        while option2 not in range(0, 8):
            option2 = int(input("Ingresa una opcion [1] al [7]:"))
        
        return option2
    
    if option == 2:
        print(submenu())
        print()
        option2 = int(input("Ingresa una opcion [1] al [7]:"))
        while option2 not in range(0, 8):
            option2 = int(input("Ingresa una opcion [1] al [7]:"))
            
        return option2

def menu():
        menu = "\n\n---------------------------Menú de opciones---------------------------\n[1] Pilas\n[2] Colas\n"
        return menu

def submenu():
        print()
        submenu = "[1] Push\n[2] Pop\n[3] Show\n[4] Eliminar\n[5] Insertar \n[6] Buscar\n[7] Salir"
        return submenu


if __name__ =="__main__":
    message  = ("\x1b[1;34m"+"««BIENVENIDO USUARIO UNEMI»»"+"\33[0m").center(80,)
    print (message)
    print(menu())
    #pila
    object = Pila(5)
    #cola
    object2 = Cola(4)
    p_c = int(input("Ingresa una opcion [1] o [2]:"))
    while p_c != 1 and p_c != 2:
            p_c = int(input("\x1b[3;31m"+"Error!"+"\33[0m"+ "\nIngresa una opcion [1] o [2]:"))

    if p_c == 1:
        while True:
            object.pila(process(p_c))
            object.size()
    elif p_c == 2:
        while True:
            object2.cola(process(p_c))
            object2.size()