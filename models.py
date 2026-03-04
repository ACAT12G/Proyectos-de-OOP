class Persona():
    def __init__(self, name, email, phone):
        self.nombre=name
        self.correo=email
        self.telefono=phone

    def login(self):
        self.nombre = str(input("Escriba su nombre."))
        self.correo = str(input("Escriba su correo."))
        self.telefono = int(input("Escriba su telefono"))

    def logout(self):
        print("Salio de su cuenta exitosamente.")

    def actualizarDatos(self):
        act = int(input("Qué quieres cambiar? 1 = Nombre. 2 = Correo. 3 = Telefono."))

        match act:
            case 1:
                self.nombre = str(input("Escriba su nuevo nombre."))
                print(f"Su nuevo nombre es {self.nombre}")
            case 2:
                self.correo = str(input("Escriba su nuevo correo."))
                print(f"Su nuevo correo es {self.correo}")
            case 3:
                self.telefono = int(input("Escriba su nuevo telefono"))
                print(f"Su nuevo telefono es {self.telefono}")
            case _: 
                print("N/A")