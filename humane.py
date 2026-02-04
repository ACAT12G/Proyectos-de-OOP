class Humano:
    def __init__(self, nombre, edad, genero):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        
    def caract(self):
        print(f"Hola, mi nombre es {self.nombre} tengo {self.edad} y soy {self.genero}.")
        
    def saludo(self):
        print("Hola, soy humano.")
    
class Programador(Humano):
    def saludo2(self):
        print("Hola soy programador.")
        
class Licenciado(Humano):
    def __init__(self, nombre, edad, genero, telefono):
        super().__init__(nombre, edad, genero)
        self.telefono=telefono
    def saludo(self):
        print("Hola, soy un lic.")
    def caract(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} y soy {self.genero}, mi numero es {self.telefono}")