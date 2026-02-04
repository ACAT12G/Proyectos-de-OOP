class Animal:
    def __init__(self, nombre, color, patas, sonido):
        self.nombre=nombre
        self.color=color
        self.patas=patas
        self.sonido=sonido
        
    def sound(self):
        print(f"{self.nombre} hace un {self.sonido}...")
        
class Conejo(Animal):
    def pres1(self):
        print(f"Mi conejo se llama {self.nombre}, es de color {self.color}, y tiene {self.patas} patas, y hace un skee!")
        
class Ormi(Animal):
    def __init__(self, nombre, color, patas, sonido, pico):
        super().__init__(nombre, color, patas, sonido)
        self.pico=pico
    def pres2(self):
        print(f"Mi ormitorrinco se llama {self.nombre}, es de color {self.color}, su pico es {self.pico} y tiene {self.patas} patas, y hace un sonido de chasqueo.")
        
class Dino(Animal):
    def __init__(self, nombre, color, patas, sonido, tipo):
        super().__init__(nombre, color, patas, sonido)
        self.tipo=tipo
    def pres2(self):
        print(f"Mi dino se llama {self.nombre}, es de color {self.color}, es un {self.tipo} y tiene {self.patas} patas, y hace un sonido de rawr.")