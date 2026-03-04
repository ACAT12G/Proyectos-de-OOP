from models import *

# 10 Personas
per1 = Persona("María", "maria.lopez@gmail.com", 555123456)
per2 = Persona("Pedro", "pedro_sanchez@yahoo.com", 555654987)
per3 = Persona("Lucía", "lucia.torres@hotmail.com", 555159753)
per4 = Persona("Diego", "diego.ramirez@outlook.com", 555357159)
per5 = Persona("Sofía", "sofia.castillo@gmail.com", 555753159)
per6 = Persona("Miguel", "miguel.herrera@yahoo.com", 555951357)
per7 = Persona("Nightflaid", "nightflaid@infernalands.com", 555000001)
per8 = Persona("Insatian", "insatian@infernalands.com", 555000002)
per9 = Persona("Atrocean", "atrocean@infernalands.com", 555000003)
per10 = Persona("Hivemine", "hivemine@infernalands.com", 555000004)

# 10 Usuarios
usu1 = Usuario("Carlos", "carlos.mendez@yahoo.com", 555987654, 100, [])
usu2 = Usuario("Laura", "laura.j@gmail.com", 555111222, 50, [])
usu3 = Usuario("Jorge", "jorge.m@hotmail.com", 555333444, 200, [])
usu4 = Usuario("Carmen", "carmen.p@yahoo.com", 555555666, 10, [])
usu5 = Usuario("Raul", "raul.v@outlook.com", 555777888, 300, [])
usu6 = Usuario("Valeria", "valeria.c@gmail.com", 555999000, 150, [])
usu7 = Usuario("Andres", "andres.r@yahoo.com", 555222333, 0, [])
usu8 = Usuario("Natalia", "natalia.g@hotmail.com", 555444555, 75, [])
usu9 = Usuario("Esteban", "esteban.l@outlook.com", 555666777, 80, [])
usu10 = Usuario("Diana", "diana.f@gmail.com", 555888999, 500, [])

# 10 Empleados
emp1 = Empleado("Ana", "ana_gomez@hotmail.com", 555456789, 12345, "Admin", "09:00 - 17:00")
emp2 = Empleado("Luis", "luis.fernandez@outlook.com", 555321654, 54321, "Taquillero", "10:00 - 18:00")
emp3 = Empleado("Elena", "elena.ruiz@gmail.com", 555789123, 45673, "Janitor", "08:00 - 16:00")
emp4 = Empleado("Mario", "mario.w@cine.com", 555010101, 10001, "Proyeccionista", "12:00 - 20:00")
emp5 = Empleado("Rosa", "rosa.k@cine.com", 555020202, 10002, "Dulceria", "14:00 - 22:00")
emp6 = Empleado("Pablo", "pablo.q@cine.com", 555030303, 10003, "Seguridad", "18:00 - 02:00")
emp7 = Empleado("Carla", "carla.z@cine.com", 555040404, 10004, "Gerente", "09:00 - 17:00")
emp8 = Empleado("Hugo", "hugo.b@cine.com", 555050505, 10005, "Taquillero", "16:00 - 00:00")
emp9 = Empleado("Irene", "irene.n@cine.com", 555060606, 10006, "Janitor", "18:00 - 02:00")
emp10 = Empleado("Omar", "omar.x@cine.com", 555070707, 10007, "Dulceria", "10:00 - 18:00")

# 10 Espacios
esp1 = Espacio(674, "Espacio x", "Primer piso")
esp2 = Espacio(675, "Pasillo A", "Primer piso")
esp3 = Espacio(676, "Lobby Principal", "Planta Baja")
esp4 = Espacio(677, "Baños Sur", "Primer piso")
esp5 = Espacio(678, "Baños Norte", "Segundo piso")
esp6 = Espacio(679, "Bodega 1", "Sotano")
esp7 = Espacio(680, "Sala de Espera VIP", "Segundo piso")
esp8 = Espacio(681, "Terraza", "Tercer piso")
esp9 = Espacio(682, "Cuarto de Proyección General", "Tercer piso")
esp10 = Espacio(683, "Salida de Emergencia Frontal", "Planta Baja")

# 10 Salas
sala1 = Sala(101, "Sala chida", "Segundo piso", tipo.TresD, 100, True)
sala2 = Sala(102, "Sala 2", "Segundo piso", tipo.DosD, 150, False)
sala3 = Sala(103, "Sala 3", "Segundo piso", tipo.DosD, 150, False)
sala4 = Sala(104, "Sala 4 MAX", "Tercer piso", tipo.Imax, 250, False)
sala5 = Sala(105, "Sala 5 VIP", "Tercer piso", tipo.DosD, 50, True)
sala6 = Sala(106, "Sala 6 3D", "Primer piso", tipo.TresD, 120, False)
sala7 = Sala(107, "Sala 7", "Primer piso", tipo.DosD, 100, False)
sala8 = Sala(108, "Sala 8", "Primer piso", tipo.DosD, 100, False)
sala9 = Sala(109, "Sala 9 Ultra", "Segundo piso", tipo.Imax, 200, False)
sala10 = Sala(110, "Sala 10 Platino", "Tercer piso", tipo.TresD, 40, True)

# 10 Zonas de Comida
comida1 = ZonaComida(423, "Pizza hot", "Tercer piso")
comida2 = ZonaComida(424, "Dulcería Central", "Planta Baja")
comida3 = ZonaComida(425, "Heladería Gelato", "Planta Baja")
comida4 = ZonaComida(426, "Café Cinema", "Segundo piso")
comida5 = ZonaComida(427, "Nachos & Dogs VIP", "Tercer piso")
comida6 = ZonaComida(428, "Bar Lounge", "Tercer piso")
comida7 = ZonaComida(429, "Crepas Finas", "Primer piso")
comida8 = ZonaComida(430, "Palomitas Express Sur", "Segundo piso")
comida9 = ZonaComida(431, "Palomitas Express Norte", "Tercer piso")
comida10 = ZonaComida(432, "Candy Shop", "Primer piso")

# 10 Peliculas
peli1 = Pelicula("Amongus", 160, "G", "Terror")
peli2 = Pelicula("TwoKinds", 120, "PG-13", "Animación")
peli3 = Pelicula("Out-of-Placers", 200, "R", "Ciencia ficción")
peli4 = Pelicula("Infernalords: The Beginning", 145, "PG-13", "Fantasía oscura")
peli5 = Pelicula("Matrix 5", 150, "R", "Acción")
peli6 = Pelicula("Shrek 6", 90, "G", "Animación")
peli7 = Pelicula("El Aro 4", 110, "R", "Terror")
peli8 = Pelicula("Spider-Man: Home", 135, "PG-13", "Acción")
peli9 = Pelicula("Interstellar Re-release", 169, "PG", "Ciencia ficción")
peli10 = Pelicula("Dune 3", 180, "PG-13", "Ciencia ficción")

# 10 Funciones
fun1 = Funcion(384, peli1, sala1, 130)
fun2 = Funcion(385, peli2, sala2, 100)
fun3 = Funcion(386, peli3, sala4, 150)
fun4 = Funcion(387, peli4, sala5, 200)
fun5 = Funcion(388, peli5, sala9, 180)
fun6 = Funcion(389, peli6, sala7, 90)
fun7 = Funcion(390, peli7, sala3, 110)
fun8 = Funcion(391, peli8, sala6, 140)
fun9 = Funcion(392, peli9, sala10, 250)
fun10 = Funcion(393, peli10, sala8, 120)

# 10 Promociones
promo1 = Promocion("VERANO10", "10% de descuento en verano", 10, "2026-08-31")
promo2 = Promocion("ESTUDIANTE", "15% para estudiantes", 15, "2026-12-31")
promo3 = Promocion("VIP50", "50% en salas VIP", 50, "2026-05-01")
promo4 = Promocion("LUNES2X1", "50% de descuento (2x1)", 50, "2026-12-31")
promo5 = Promocion("CUMPLEAÑERO", "100% descuento en tu boleto", 100, "2026-12-31")
promo6 = Promocion("INFERNALANDS", "20% en cine de fantasía", 20, "2026-10-31")
promo7 = Promocion("TERROR15", "15% en películas de terror", 15, "2026-11-02")
promo8 = Promocion("MATINEE", "30% de descuento antes de las 2PM", 30, "2026-06-30")
promo9 = Promocion("SOCIO_ORO", "25% clientes frecuentes", 25, "2027-01-01")
promo10 = Promocion("BLACKFRIDAY", "40% de descuento general", 40, "2026-11-30")

# 10 Reservas
res1 = Reserva(1001, usu1, fun1, 130.0, estado.Pendiente)
res2 = Reserva(1002, usu2, fun2, 100.0, estado.Pagada)
res3 = Reserva(1003, usu3, fun3, 300.0, estado.Pendiente)
res4 = Reserva(1004, usu4, fun4, 200.0, estado.Pagada)
res5 = Reserva(1005, usu5, fun5, 180.0, estado.Cancelada)
res6 = Reserva(1006, usu6, fun6, 180.0, estado.Pagada)
res7 = Reserva(1007, usu7, fun7, 110.0, estado.Pendiente)
res8 = Reserva(1008, usu8, fun8, 280.0, estado.Pagada)
res9 = Reserva(1009, usu9, fun9, 500.0, estado.Cancelada)
res10 = Reserva(1010, usu10, fun10, 120.0, estado.Pagada)

print("\n--- REGISTRO MANUAL DE INVENTARIO (10 OBJETOS) ---")
lista_pelis = [peli1, peli2, peli3, peli4, peli5, peli6, peli7, peli8, peli9, peli10]

for i, p in enumerate(lista_pelis, 1):
    print(f"ID: {i}")
    print(f"{p.titulo} ({p.duracion} min)")
    print(f"Cat: {p.genero}")
print("\n--- VALIDACIÓN DE DATOS FINALIZADA ---")

# Metodos indivuales.

# Usuarios y Empleados.
usu1.consultarPromociones()
usu1.crearReserva(res1)
usu1.cancelarReserva(res1)

emp2.marcarEntrada()
emp1.gestionarFunciones()
emp3.gestionarFunciones()

# Espacios y Salas.
esp1.verificarDisponibilidad()
esp1.limpiarEspacio()

sala1.verificarDisponibilidad()
sala1.limpiarEspacio()
sala1.obtenertiposala()

# Películas y Funciones.
peli1.esAptaParaTodoPublico()
peli3.esAptaParaTodoPublico()
peli2.obtenerSinopsis()
peli4.obtenerSinopsis()

fun1.calcularAsientosLibres()
fun1.obtenerDetallesFuncion()

# Promociones y Reservas.
print(f"¿Promoción {promo1.codigo} es válida?: {promo1.esValida()}")
print(f"¿Promoción {promo9.codigo} es válida?: {promo9.esValida()}")

res1.aplicarPromocion(promo1)
res1.confirmarPago()
res1.generarticket()

print("Ticket de reserva prepago.")
res2.generarticket()

usu1 = Usuario("Carlos88", "carlos@yahoo.com", 555987654, 150, [])
emp1 = Empleado("Ana", "ana_gomez@hotmail.com", 555456789, 12345, "Admin", "09:00 - 17:00")
sala4 = Sala(4, "Sala 04", "Tercer piso", tipo.Imax, 250, False)
fun10 = Funcion(393, peli10, sala4, 450.0)
promo_est = Promocion("PROMO_ESTUDIANTE", "20% para estudiantes", 20, "2026-12-31")

# Reto 1 y 2.
print("\n----------------------------------------------")
print(f"Usuario: {usu1.nombre} (Puntos: {usu1.puntosFidelidad})")
print(f"Película: '{fun10.pelicula.titulo}' | Sala: {fun10.sala.nombre} ({fun10.sala.tipo.value})")

asientos_ocupados_fun10 = ["A2", "C4", "D1"] 

asientos_solicitados = ["A1", "A2", "B5"]
print(f"Seleccione los asientos (separados con coma): {', '.join(asientos_solicitados)}")

asientos_validos = []
for asiento in asientos_solicitados:
    if asiento in asientos_ocupados_fun10:
        print(f"El asiento {asiento} ya está ocupado por otra reserva.")
    else:
        asientos_validos.append(asiento)

if len(asientos_validos) < len(asientos_solicitados):
    print("Solo asientos libres.")
    asientos_solicitados = ["A1", "A3", "B5"]
    print(f"Seleccione los asientos: {', '.join(asientos_solicitados)}")
    
    asientos_validos = [a for a in asientos_solicitados if a not in asientos_ocupados_fun10]

print(f"Asientos {', '.join(asientos_validos)} bloqueados con éxito.")

res_reto = Reserva(995, usu1, fun10, fun10.precioBase, estado.Pendiente)
res_reto.asientos = asientos_validos
asientos_ocupados_fun10.extend(asientos_validos) 

print(f"Monto base: ${res_reto.montoTotal:.2f}")

print("\n--------------------------------------------------")

if emp1.rol in ["Admin", "Gerente"]:
    print("Binvenido, admin.")
    nueva_peli = Pelicula("Cinco noches con Alfredo", 110, "PG-13", "Terror")
    print(f"Película '{nueva_peli.titulo}' agregada al catálogo.")
    nueva_funcion = Funcion(400, nueva_peli, sala4, 120.0)
    print(f"Función {nueva_funcion.idFuncion} creada para '{nueva_peli.titulo}' en '{sala4.nombre}'.")
    nueva_promo = Promocion("HALLOWEEN", "Descuento del 30%", 30, "2026-10-31")
    print(f"Promoción '{nueva_promo.codigo}' dada de alta en el sistema.")
else:
    print("No tienes permisos para esto.")

if promo_est.esValida():
    res_reto.aplicarPromocion(promo_est)

res_reto.confirmarPago()
print("\n--- TICKET GENERADO ---")
res_reto.generarticket()