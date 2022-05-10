import copy

from termcolor import colored

from Domain.entities import student


class studenti_repo:
    def __init__(self):
        self.__studenti = []

    def actualizeaza(self, lista):
        for elem in lista:
            self.__studenti.append(elem)

    def adauga(self, stud):
        self.__studenti.append(stud)

    def getclasa(self):
        return self.__studenti

    def getstudent_clasa(self, index):
        return self.__studenti[index]

    def afiseaza(self):
        for elem in self.__studenti:
            print(elem)


class fisier_studenti_repo:
    def __init__(self, filename):
        self.__filename = filename

    def citeste_student(self):
        try:
            f = open(self.__filename, 'r')
            fisier = f.read()
            f.close()
            entitati = fisier.split('\n')
            for line in entitati:
                stud = self.creeaza_student_line(line)
            return stud
        except IOError:
            print(colored("Fisierul nu exista", 'red'))

    def creeaza_student_line(self, line):
        line = line.split(' ')
        id = line[0]
        nume = line[1]
        grupa = line[2]
        stud = student(id,nume, grupa)
        return stud

    def load_from_file(self):
        try:
            f = open(self.__filename, 'r')
            fisier = f.read()
            f.close()
            lista = []
            entitati = fisier.split('~')
            for line in entitati:
                stud = self.creeaza_student_line(line)
                lista.append(stud)
            return lista
        except IOError:
            print(colored("Fisierul nu exista", 'red'))


    def scrie_in_fisier(self, elem):
        f = open(self.__filename, "a")
        f.write("\n")
        f.write("Studentul este: ")
        f.write("\n")
        f.write(elem)
        f.close()

    def scrie_in_fisier_lista(self, lista):
        f = open(self.__filename, "a")
        f.write("\n")
        f.write("Studentii sunt:")
        f.write("\n")
        for elem in lista:
            f.write(str(elem))
            f.write("\n")
        f.close()


def test_clasa_adauga_student():
    s1 = student(12, "Marcel Mihai", 13)
    s2 = student(312, "Marceli", 132)
    c1 = studenti_repo()
    c1.adauga(s1)
    c1.adauga(s2)
    assert (c1.getstudent_clasa(0) == s1)
    assert (c1.getstudent_clasa(1) == s2)
