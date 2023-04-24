class Libro:
    def __init__(self, id, titulo, autor, genero, editorial, tramo):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.editorial = editorial
        self.tramo = tramo
        self.prestado = False

class Biblioteca:
    def __init__(self):
        self.libros = [
            Libro(1, "El guardián entre el centeno", "J.D. Salinger", "Ficción", "Little", "1"),
            Libro(2, "Matar a un ruiseñor", "Harper Lee", "Ficción", "J. B.", "2"),
            Libro(3, "El gran Gatsby", "F. Scott Fitzgerald", "Ficción", "Charles", "3"),
            Libro(4, "Orgullo y prejuicio", "Jane Austen", "Ficción", "T. Egerton", "4"),
            Libro(5, "1984", "George Orwell", "Ficción", "Secker", "5")
        ]
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print("Libro agregado con éxito.")
    
    def modificar_libro(self, id):
        for libro in self.libros:
            if libro.id == id:
                libro.titulo = input("Nuevo título: ")
                libro.autor = input("Nuevo autor: ")
                libro.genero = input("Nuevo género: ")
                libro.editorial = input("Nueva editorial: ")
                libro.tramo = input("Nuevo tramo: ")
                print("Libro modificado con éxito.")
                return
        print("Libro no encontrado.")
    
    def listar_libros(self):
        print("{:<10} {:<30} {:<20} {:<15} {:<15} {:<10} {:<10}".format("ID", "Titulo", "Autor", "Genero", "Editorial", "Tramo", "Prestado"))
        for libro in self.libros:
            prestado_str = "Sí" if libro.prestado else "No"
            print("{:<10} {:<30} {:<20} {:<15} {:<15} {:<10} {:<10}".format(libro.id, libro.titulo, libro.autor, libro.genero, libro.editorial, libro.tramo, prestado_str))
    
    def buscar_libro_por_id(self, id):
        for libro in self.libros:
            if libro.id == id:
                prestado_str = "Sí" if libro.prestado else "No"
                print(f"ID: {libro.id}\nTítulo: {libro.titulo}\nAutor: {libro.autor}\nGénero: {libro.genero}\nEditorial: {libro.editorial}\nTramo: {libro.tramo}\nPrestado: {prestado_str}")
                return
        print("Libro no encontrado.")
    
    def borrar_libro(self, id):
        for libro in self.libros:
            if libro.id == id:
                self.libros.remove(libro)
                print("Libro borrado con éxito.")
                return
        print("Libro no encontrado.")
    
    def tomar_prestado(self, id):
        for libro in self.libros:
            if libro.id == id:
                if not libro.prestado:
                    libro.prestado = True
                    print(f"El libro '{libro.titulo}' ha sido tomado prestado con éxito.")
                    return
                else:
                    print("Lo siento, el libro ya ha sido prestado.")
                    return
        print("Lo siento, no se encontró ningún libro con ese ID.")

    def devolver_libro(self, id):
        for libro in self.libros:
            if libro.id == id:
                if libro.prestado:
                    libro.prestado = False
                    print(f"El libro '{libro.titulo}' ha sido devuelto.")
                    return
                else:
                    print("Lo siento, el libro no ha sido prestado.")
                    return
        print("Lo siento, no se encontró ningún libro con ese ID.")

def mostrar_menu():
        print("Gestor de Biblioteca")
        print("1. Agregar un libro")
        print("2. Modificar un libro")
        print("3. Lista de libros")
        print("4. Buscar libro por ID")
        print("5. Borrar libro")
        print("6. Tomar prestado un libro")
        print("7. Devolver un libro")
        print("8. Salir")

biblioteca = Biblioteca()

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        id = int(input("ID: "))
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Género: ")
        editorial = input("Editorial: ")
        tramo = input("Tramo: ")
        libro = Libro(id, titulo, autor, genero, editorial, tramo)
        biblioteca.agregar_libro(libro)
    elif opcion == "2":
        id = int(input("ID del libro a modificar: "))
        biblioteca.modificar_libro(id)
    elif opcion == "3":
        biblioteca.listar_libros()
    elif opcion == "4":
        id = int(input("ID del libro a buscar: "))
        biblioteca.buscar_libro_por_id(id)
    elif opcion == "5":
        id = int(input("ID del libro a borrar: "))
        biblioteca.borrar_libro(id)
    elif opcion == "6":
        id = int(input("ID del libro a tomar prestado: "))
        biblioteca.tomar_prestado(id)
    elif opcion == "7":
        id = int(input("ID del libro a devolver: "))
        biblioteca.devolver_libro(id)
    elif opcion == "8":
        break
    else:
        print("Opción inválida.")
    
    input("Presione enter para continuar...")

print("¡Gracias por usar la biblioteca!") 