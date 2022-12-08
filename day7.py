from typing import List
from getdata import getdata


class Fichero:
    directorio_padre = None
    nombre: str
    tamanho = None
    gestor = None

    def __init__(self, nombre, tamanho, directorio_padre, gestor):
        self.nombre = nombre
        self.tamanho = int(tamanho)
        self.directorio_padre = directorio_padre
        self.gestor = gestor

    def get_size(self):
        return self.tamanho

    def __repr__(self):
        return f'Fichero: {self.nombre}'


class Directorio(Fichero):
    ficheros_hijos: List[Fichero]

    def __init__(self, nombre, directorio_padre, gestor):
        super().__init__(nombre, 0, directorio_padre, gestor)
        self.ficheros_hijos = []

    def get_size(self):
        if self.tamanho != 0:
            return self.tamanho
        tamano_total = 0
        for fichero in self.ficheros_hijos:
            tamano_total += fichero.get_size()

        self.tamanho = tamano_total

        self.gestor.tamanhos.append(tamano_total)
        return tamano_total

    def get_fichero(self, dir: str):
        for fich in self.ficheros_hijos:
            if fich.nombre == dir:
                return fich

    def __repr__(self):
        return f'Directorio: {self.nombre}'


class GestorSistemaFich:
    dir_act: Directorio
    root: Directorio

    tamanhos = []

    def __init__(self):
        self.directorios = {}
        root = Directorio('/', None, self)
        self.directorios['/'] = root
        self.dir_act = root
        self.root = root

    def cd(self, dir: str):
        if dir == '..':
            self.dir_act = self.dir_act.directorio_padre
        elif dir == '/':
            self.dir_act = self.root
        else:
            self.dir_act = self.dir_act.get_fichero(dir)

    def insertar_fichero(self, nombre, tam):
        self.dir_act.ficheros_hijos.append(Fichero(nombre, tam, self.dir_act, self))

    def insertar_dir(self, dir: str):
        directorio = Directorio(dir, self.dir_act, self)
        self.dir_act.ficheros_hijos.append(directorio)
        self.directorios[dir] = directorio




def parse(instruccion: str):
    list_instr = instruccion.split(' ')
    if len(list_instr) == 2:
        return list_instr[0], list_instr[1]
    else:
        return list_instr[0]


def ejecutar_input(instruccion: str, gestor: GestorSistemaFich):
    mandato, param = parse(instruccion)
    if mandato == 'cd':
        gestor.cd(param)


def guardar_informacion(instrucion, gestor: GestorSistemaFich):
    tam, nombre = parse(instrucion)
    if tam == 'dir':
        gestor.insertar_dir(nombre)
    else:
        gestor.insertar_fichero(nombre, tam)


def construir_arbol(data: List[str], gestor):
    for instrucion in data:
        if instrucion.startswith('$'):
            ejecutar_input(instrucion[2:], gestor)
        else:
            guardar_informacion(instrucion, gestor)

content = getdata.getdata('day7')
content = getdata.separarPorLineas(content)

gestor = GestorSistemaFich()

construir_arbol(content, gestor)


def first_star(gestor: GestorSistemaFich):
    gestor.root.get_size()
    return sum([tam for tam in gestor.tamanhos if tam < 100000])


def second_star(gestor: GestorSistemaFich):
    tam_minimo = 30000000
    tam_disp = 70000000 - gestor.root.get_size()
    min_borrar = gestor.root.get_size()
    for tam in gestor.tamanhos:
        if tam_disp + tam >= tam_minimo:
            min_borrar = min(min_borrar, tam)
    return min_borrar


print(first_star(gestor))
