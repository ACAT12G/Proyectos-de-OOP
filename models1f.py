import random
from enum import Enum
import datetime

class Persona():
    def __init__(self, name, email, phone):
        self.nombre=name
        self.correo=email
        self.telefono=phone

    def login(self):
        while True:
            nuevo_nombre = input("Escriba su nombre: ")
            if nuevo_nombre.strip() == "": 
                print("El nombre no puede estar vacío.")
                self.nombre = "Anon"
                break
            else:
                self.nombre = nuevo_nombre
                print(f"Su nuevo nombre es {self.nombre}")
                break
        while True:
            try:
                self.telefono = int(input("Escriba su nuevo telefono: "))
                print(f"Su nuevo telefono es {self.telefono}")
                break
            except ValueError:
                print("El telefono debe ser un numero entero.")
                self.telefono = 123456789
        while True:
            nuevo_correo = input("Escriba su nuevo correo: ")
            if nuevo_correo.strip() == "":
                print("El correo no puede estar vacío.")
                self.correo = "anon@gmail.com"
                break
            else:
                self.correo = nuevo_correo
                print(f"Su nuevo correo es {self.correo}")
                break

    def logout(self):
        print(f"El usuario {self.nombre} salió de su cuenta exitosamente.")

    def actualizarDatos(self):
        act = int(input("1 = Nombre. 2 = Correo. 3 = Telefono - Vas a cambiar?: "))

        match act:
            case 1:
                while True:
                    nuevo_nombre = input("Escriba su nombre: ")
                    if nuevo_nombre.strip() == "":
                        print("El nombre no puede estar vacío.")
                    else:
                        self.nombre = nuevo_nombre
                        print(f"Su nuevo nombre es {self.nombre}")
                        break
            case 2:
                while True:
                    nuevo_correo = input("Escriba su nuevo correo: ")
                    if nuevo_correo.strip() == "":
                        print("El correo no puede estar vacío.")
                    else:
                        self.correo = nuevo_correo
                        print(f"Su nuevo correo es {self.correo}")
                        break
            case 3:
                while True:
                    try:
                        self.telefono = int(input("Escriba su nuevo telefono: "))
                        print(f"Su nuevo telefono es {self.telefono}")
                        break
                    except ValueError:
                        print("Error: El telefono debe ser un numero entero. Intenta de nuevo.")
            case _: 
                print("N/A")

class Usuario(Persona):
    def __init__(self, name, email, phone, puntosFidelidad, historialReservas):
        super().__init__(name, email, phone)
        self.puntosFidelidad = puntosFidelidad
        self.historialReservas = list(historialReservas)

    def crearReserva(self, reserva):
        self.historialReservas.append(reserva)
        print(f"Reserva creada: {reserva}")

    def consultarPromociones(self):
        print("Promociones disponibles: 10% de descuento en tu próxima reserva.")

    def cancelarReserva(self, reserva):
        if reserva in self.historialReservas:
            self.historialReservas.remove(reserva)
            print(f"Reserva cancelada: {reserva}")
        else:
            print("Reserva no encontrada en el historial.")

class Empleado(Persona):
    def __init__(self, name, email, phone, idEmpleado, rol, horario):
        super().__init__(name, email, phone)
        self.idEmpleado = idEmpleado
        self.rol = rol
        self.horario = horario

    def marcarEntrada(self):
        self.horario = "Entrada marcada a las 9:00 AM"
        print(self.horario)

    def gestionarFunciones(self, Funcion):
        if self.rol == "Admin":
            print(Funcion.obtenerDetallesFuncion())
            act2 = int(input("Qué quieres hacer? Modificar = 1.- Pelicula. 2.- Sala. 3.- Precio. "))
            match act2:
                case 1:
                    Funcion.pelicula.obtenerSinopsis()
                    Funcion.pelicula.esAptaParaTodoPublico()
                    question = input("Quieres cambiar la pelicula? (s/n): ")
                    if question.lower() == "s": 
                        nuevo_titulo = input("Escribe el nuevo titulo: ")
                        nuevo_duracion = int(input("Escribe la nueva duracion (en minutos): "))
                        nueva_clasificacion = input("Escribe la nueva clasificacion (Solo PG o G para que sea apta para todos.): ")
                        nuevo_genero = input("Escribe el nuevo genero: ")
                        Funcion.pelicula = Pelicula(nuevo_titulo, nuevo_duracion, nueva_clasificacion, nuevo_genero)
                        print(f"Película actualizada a: {Funcion.pelicula.titulo}, {Funcion.pelicula.duracion}min, {Funcion.pelicula.clasificacion}, {Funcion.pelicula.genero}")
                    else:
                        print("Nada.")
                case 2:
                    Funcion.sala.ajustarAforo()
                    Funcion.sala.obtenertiposala()
                    question2 = input("Quieres cambiar el tipo de sala? (s/n): ")
                    if question2.lower() == "s":   
                        nuevo_tipo = input("Escribe el nuevo tipo de sala (2D, 3D, IMAX): ")
                        if nuevo_tipo in tipo._value2member_map_:
                            Funcion.sala.tipo = tipo(nuevo_tipo)
                            print(f"Tipo de sala actualizado a: {Funcion.sala.tipo.value}")
                        else:
                            print("Nada.")
                case 3:
                    nuevo_precio = float(input("Escribe el nuevo precio base: "))
                    Funcion.precioBase = nuevo_precio
                    print(f"Precio base actualizado a: ${Funcion.precioBase:.2f}")
                case _:
                    print("Nada.")
        else:
            print("No eres admin.")

# ----------------------------------------------------------------------------------
class Espacio():
    def __init__(self, idEspacio, nombre, ubicacion):
        self.idEspacio = idEspacio
        self.nombre = nombre
        self.ubicacion = ubicacion

    def verificarDisponibilidad(self):
        resultado = random.choice([True, False])
        if resultado:
            print(f"El espacio {self.nombre} está disponible.")
        else:
            print(f"El espacio {self.nombre} no está disponible.")

    def limpiarEspacio(self):
        print(f"El espacio {self.nombre} ha sido limpiado.") #No entiedno muy bien el proposito de esta.

class tipo (Enum):
    DosD = "2D"
    TresD = "3D"
    Imax = "IMAX"

class Sala(Espacio):
    def __init__(self, idEspacio, nombre, ubicacion, tipo, capacidadTotal, esVIP):
        super().__init__(idEspacio, nombre, ubicacion)
        self.tipo = tipo
        self.capacidadTotal = capacidadTotal
        self.esVIP = esVIP

    def ajustarAforo(self):
        ajuste = int(input("Cuanto quiere ajustar la sala? Nuevo aforo: "))
        self.capacidadTotal = ajuste

    def obtenertiposala(self):
        print(f"El tipo de sala es: {self.tipo.value}")

class ZonaComida(Espacio):
    def __init__(self, idEspacio, nombre, ubicacion):
        super().__init__(idEspacio, nombre, ubicacion)
        self.listaProductos = []
        self.stockActual = {}

    def actualizarInventario(self):
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        if producto in self.stockActual:
            self.stockActual[producto] += cantidad
        else:
            self.stockActual[producto] = cantidad
            self.listaProductos.append(producto)
        print(f"Inventario actualizado: {self.stockActual}")

    def venderProducto(self):
        producto = input("Qué vas a vender?: ")
        if producto in self.stockActual and self.stockActual[producto] > 0:
            self.stockActual[producto] -= 1
            print(f"Producto vendido!")
        else:
            print("Ya no hay.")

#--------------------------------------------------------------------------------------
class Pelicula:
    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.genero = genero

    def obtenerSinopsis(self):
        ran = random.choice([1, 2, 3])
        if ran == 1:
            print("BNA: Brand New Animal es una serie de anime original producida por el estudio japonés Trigger, dirigida por Yoh Yoshinari y escrita por Kazuki Nakashima.  La historia se desarrolla en el siglo XXI, cuando la existencia de seres humanos antropomorfos, conocidos como beastmen, sale a la luz tras vivir en secreto durante siglos. ")
        elif ran == 2:
            print("TwoKinds es un webcómic de fantasía medieval creado por Thomas Fischbach que sigue las aventuras de Trace Legacy, un humano amnésico y ex-líder de la organización mágica Templar, y su compañera Flora, una tigresa Keidran ex-esclava.")
        else:
            print("Out-of-Placers (OoPs) is an anthromorphic transformation fiction webcomic by Valsalia. The comic follows Kassen Akoll, initially a human guardsman in the employ of House Ivenmoth. A mysterious artifact changes both his species and gender into a yinglet, a rat-like scavenging sapient species. Kass must now navigate a new society and come to terms with the aftermath of her change.")

    def esAptaParaTodoPublico(self):
        if self.clasificacion in ["G", "PG"]:
            print(f"{self.titulo} es apta para todo público.")
        else:
            print(f"{self.titulo} no es apta para todo público.")

class Funcion:
    def __init__(self, idFuncion, pelicula, sala, precioBase):
        self.idFuncion = idFuncion
        self.pelicula = pelicula
        self.sala = sala
        self.precioBase = precioBase
        self.horarioInicio = datetime.datetime.now()

    def calcularAsientosLibres(self):
        luck = random.randint(0, self.sala.capacidadTotal)
        asientosLibres = self.sala.capacidadTotal - luck
        print(f"Asientos libres para la función {self.idFuncion}: {asientosLibres}")

    def obtenerDetallesFuncion(self):
        print(f"Detalles de la función {self.idFuncion}:")
        print(f"Película: {self.pelicula.titulo}")
        print(f"Sala: {self.sala.nombre}")
        print(f"Precio base: ${self.precioBase}")
        print(f"Horario de inicio: {self.horarioInicio.strftime('%Y-%m-%d %H:%M:%S')}") #Esta si le pedi ayuda a Gemini. ;)

#--------------------------------------------------------------------------------------
class Promocion:
    def __init__(self, codigo, descripcion, porcentajeDescuento, fechaExpiracion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.porcentajeDescuento = porcentajeDescuento
        self.fechaExpiracion = datetime.datetime.strptime(fechaExpiracion, "%Y-%m-%d")

    def esValida(self):
        if datetime.datetime.now() < self.fechaExpiracion:
           return True
        else:
           return False

class estado(Enum):
    Pendiente = "Pendiente"
    Pagada = "Pagada"
    Cancelada = "Cancelada"

class Reserva:
    def __init__(self, idReserva, usuario, funcion, montoTotal, estado):
        self.idReserva = idReserva
        self.usuario = usuario
        self.funcion = funcion
        self.montoTotal = montoTotal
        self.estado = estado
        self.asientos = []

    def confirmarPago(self):
        if self.estado == estado.Pendiente:
            self.estado = estado.Pagada
            print(f"Reserva {self.idReserva} ha sido pagada.")
        else:
            print("Ya esta pagada o cancelada.")

    def generarticket(self):
        if self.estado == estado.Pagada:
            print(f"Ticket para {self.idReserva}.")
            print(f"Usuario: {self.usuario.nombre}")
            print(f"Película: {self.funcion.pelicula.titulo}")
            print(f"Sala: {self.funcion.sala.nombre}")
            print(f"Horario: {self.funcion.horarioInicio.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Asientos: {', '.join(self.asientos)}")
            print("¡Disfruta tu película!")
        else:
            print("La reserva no ha sido pagada. No se puede generar el ticket.")

    def aplicarPromocion(self, promocion):
        if promocion.esValida():
            descuento = self.montoTotal * (promocion.porcentajeDescuento / 100)
            self.montoTotal -= descuento
            print(f"Código: {promocion.codigo} (-{promocion.porcentajeDescuento}%)")
            print(f"Precio final: ${self.montoTotal:.2f}")
