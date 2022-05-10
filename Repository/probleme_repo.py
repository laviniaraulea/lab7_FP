import copy

from termcolor import colored

from Domain.entities import laborator


class probleme_repo:
    def __init__(self):
        self.__probleme = []

    def getprobleme(self):
        return self.__probleme

    def getproblema_index(self, index):
        return self.__probleme[index]

    def adauga(self, prob):
        self.__probleme.append(prob)

    def afiseaza(self):
        for elem in self.__probleme:
            print(elem)

    def actualizeaza(self, lista):
       for elem in lista:
           self.__probleme.append(elem)


class fisier_probleme_repo:
    def __init__(self, filename):
        self.__filename = filename

    def citeste_problema(self):
        try:
            f = open(self.__filename, 'r')
            fisier = f.read()
            entitati = fisier.split('\n')
            for line in entitati:
                prob = self.creeaza_probleme_line(line)
            return prob
        except IOError:
            print(colored("Fisierul nu exista", 'red'))
        finally:
            f.close()

    def creeaza_probleme_line(self, line):
        line = line.split(",")
        lab = laborator(line[0], line[1], line[2])
        return lab

    def load_from_file(self):
        try:
            f = open(self.__filename, 'r')
        except IOError:
            print(colored("Fisierul nu exista", 'red'))
        fisier = f.read()
        f.close()
        lista = []
        entitati = fisier.split('\n')
        for line in entitati:
            lab = self.creeaza_probleme_line(line)
            lista.append(lab)
        return lista

    def scrie_in_fisier(self, elem):
        f = open(self.__filename, "a")
        f.write("\n")
        f.write("Laboratorul este: ")
        f.write("\n")
        f.write(elem)
        f.close()

    def scrie_in_fisier_lista(self, lista):
        f = open(self.__filename, "a")
        f.write("\n")
        f.write("Laboratoarele sunt:")
        f.write("\n")
        for elem in lista:
            f.write(str(elem))
            f.write("\n")
        f.close()
