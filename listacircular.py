#Circular

class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class listacircularsimple:

    def __init__(self):
        self.primero = None
        self.ultimo = None
#Creamos una funcion para ver si la lista esta vacia o no 
    def vacia(self):
        return self.primero == None
    #agregar al final
    def agregar_final(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.primero.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.siguiente = self.primero

#eliminar final                 
    def eliminar_final(self):
        if self.vacia():
            print("Lista vacía")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            aux = self.primero
            while aux.siguiente != self.ultimo:
                aux = aux.siguiente
            aux.siguiente = self.primero
            self.ultimo = aux
    #mostrar elementos 
    def mostrar(self):
            aux = self.primero
            while aux:
                print(aux.dato)
                aux = aux.siguiente
                if aux == self.primero:
                    break
    
    #agregar inicio
    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.primero.siguiente = self.primero
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux
            self.ultimo.siguiente = self.primero
    #eliminar inicio
    def eliminar_inicio(self):
        if self.vacia():
            print("Lista vacía")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.ultimo.siguiente = self.primero

#menú de opciones
try:
    if __name__ == "__main__":
        opcion = 0
        lista = listacircularsimple()
        while opcion != 7:
            print("--- LISTA SIMPLE CIRCULAR ENLAZADA ---\n 1. Agregar final\n 2. Eliminar final\n 3. Mostrar\n 4. Agregar Inicio\n 5. Eliminar Inicio\n 6. ¿La lista está vacia?\n 7. Salir")
            opcion = int(input("Ingrese su opción "))

            if opcion == 1:
                dato = input("Ingresa un número ")
                lista.agregar_final(dato)
            elif opcion == 2:
                lista.eliminar_final()
            elif opcion == 3:
                lista.mostrar()
            elif opcion == 4:
                dato = input("Ingresa un número ")
                lista.agregar_inicio(dato)
            elif opcion == 5:
                lista.eliminar_inicio()
            elif opcion == 6:
                print("SI" if lista.vacia() else "NO")
            elif opcion == 7:
                print("Finalizado")
            else:
                print("vuelve a intentarlo.")
except Exception as e:
    print(e)