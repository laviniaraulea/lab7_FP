import copy

from termcolor import colored

from Domain.entities import student, laborator, nota


class clasa_de_legatura_repo:
    def __init__(self):
        self.__note = []

    def actualizeaza(self, lista):
        '''
        Actualizeaza note_repo-ul cu o lista nota
        :param lista: lista care se copiaza
        :return: -
        '''
        self.__note = copy.deepcopy(lista)

    def adauga_nota(self, nota):
        self.__note.append(nota)

    def getnote(self):
        return self.__note

    def getnota(self, index):
        return self.__note[index]

    def afiseaza_nota(self, index):
        print(self.__note[index])

    def afiseaza(self):
        for elem in self.__note:
            print(elem)


class fisier_clasa_de_legatura_repo:
    def __init__(self, filename):
        self.__filename = filename

    def citeste_nota(self):
        try:
            f = open(self.__filename, 'r')
            fisier = f.read()
            f.close()
            entitati = fisier.split('\n')
            for line in entitati:
                asign = self.creeaza_nota_line(line)
            return asign
        except IOError:
            print(colored("Fisierul nu exista", 'red'))

    def creeaza_nota_line(self, line):
        line = line.split(',')
        stud=student(line[0],line[1],line[2])
        lab=laborator(line[3],line[4],line[5])
        n = line[6]
        asignare = nota(stud, lab, n)
        return asignare

    def load_from_file(self):
        try:
            f = open(self.__filename, 'r')
            fisier = f.read()
            f.close()
            lista = []
            entitati = fisier.split('\n')
            for line in entitati:
                asign = self.creeaza_nota_line(line)
                lista.append(asign)
            return lista
        except IOError:
            print(colored("Fisierul nu exista", 'red'))

    def scrie_in_fisier(self, elem):
        f = open(self.__filename, "a")
        f.write("\n")
        f.write("Asignarea este: ")
        f.write("\n")
        f.write(elem)
        f.close()

    def scrie_in_fisier_lista(self, lista):
        f = open(self.__filename, "a")
        f.write("\n")
        f.write("Asignarile sunt:")
        f.write("\n")
        for elem in lista:
            f.write(str(elem))
            f.write("\n")
        f.close()


