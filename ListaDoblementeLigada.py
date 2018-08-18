class ListaDoblementeLigada(object):

    class Nodo(object):
        elemento = None
        anterior = None
        siguiente = None

        def __init__(self, elemento):
            self.elemento = elemento

        def get_anterior(self):
            return anterior

        def get_siguiente(self):
            return siguiente

        def get(self):
            return elemento


cabeza = None
rabo = None
longitud = 0

def get_longitud():
    return longitud

def es_vacia():
    if longitud == 0:
        return True
    else:
        return False

def agrega_final(elemento):
    nuevo = Nodo(elemento)
    if (es_vacia):
        cabeza = rabo = nuevo
        longitud += 1
    else:
        rabo.siguiente = nuevo
        n.siguente = rabo
        rabo = n

def agrega_inicio(elemento):
    nuevo = Nodo(elemento)
    if (es_vacia):
        cabeza = rabo = nuevo
        longitud += 1
    else:
        nuevo.siguiente = cabeza
        cabeza.anterior = nuevo
        cabeza = n

def obtener_nodo_por_indice(self, indice):
        n = cabeza
        i = 0

        while (n is not None):
            if (i == indice):
                return n
            else:
                n = n.siguiente
                i += 1
        return None

def inserta(indice, elemento):
    nuevo =  Nodo(elemento)
    if (es_vacia):
        agrega_inicio(elemento)
    elif (i == longitud):
        agrega_final(elemento)
    else:
        n = obtener_nodo_por_indice(indice)
        n.anterior.siguiente = nuevo
        nuevo.anterior = n.anterior
        n.anterior = nuevo
        nuevo.siguiente = n

def elimina(elemento):
    if (longitud == 1):
        cabeza = None
        rabo = None
        longitud = 0
    else:
        n = cabeza
        while (n != elemento):
            n = n.siguiente
        n.siguiente.anterior = n.anterior
        n.anterior.siguiente = n.siguiente
        e.siguiente = None
        e.anterior = None
        longitud -= 1

def elimina_primero():
    if es_vacia:
        return
    else:
        cabeza = cabeza.siguiente
        elem = cabeza.anterior.elemento
        cabeza.anterior.siguiente = None
        cabeza.anterior = None
        longitud -= 1
        return elem

def elimina_ultimo():
    if es_vacia:
        return
    else:
        rabo = rabo.anterior
        elem = rabo.siguiente
        rabo.siguiente.anterior = None
        rabo.suiguiente = None
        longitud -= 1
        return elem

def contiene(elemento):
    m = cabeza
    if (es_vacia()):
        return False
    while (m != None):
        if (m.elemento == elemento):
            return True
        else:
            m = m.siguiente
    return False

def reversa():
    reversa = ListaDoblementeLigada()
    m = rabo
    if es_vacia:
        return
    for i in range(0, longitud):
        reversa.agregaFinal(m.elemento)
        m = m.anterior
    return reversa

def copia():
    copia = ListaDoblementeLigada()
    m = cabeza
    if es_vacia:
        return
    for i in range(0, longitud):
        reversa.agregaFinal(m.elemento)
        m = m.suiguiente
    return copia

def limpia():
    cabeza = None
    rabo = None
    longitud = 0

def get_primero():
    if es_vacia:
        return
    else:
        return cabeza.get()

def get_ultimo():
        if es_vacia:
            return
        else:
            return rabo.get()

def get(indice):
    if es_vacia:
        return
    else:
        m = obtener_nodo_por_indice
        return m.get()

def get_cabeza():
    if es_vacia:
        return
    return cabeza

def get_rabo():
    if es_vacia:
        return
    return rabo

def to_String():
    pass
