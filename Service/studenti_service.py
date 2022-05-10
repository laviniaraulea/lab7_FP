import string
import random

from Domain.entities import student
from Domain.validatori import validator_student
from Repository.studenti_repo import studenti_repo, fisier_studenti_repo


class service_student:
    nr_studenti = 0

    def __init__(self, studenti_repo, validator_student):
        self.__stud_repo = studenti_repo
        self.__validator_student = validator_student

    def actualizeaza(self, lista):
        self.__stud_repo.actualizeaza(lista)

    def creere_student(self, id, nume, grupa):
        '''
        creaza student si valideaza datele
        :param id: id studentului
        :param nume: numele studentului
        :param grupa: grupa studentului
        :return: adauga studentul in student_repo
        '''
        stud = student(id, nume, grupa)
        if self.__validator_student.valideaza_id(stud, self.__stud_repo) and self.__validator_student.valideaza_nume(
                stud) and self.__validator_student.valideaza_grupa(stud):
            service_student.nr_studenti += 1
            self.__stud_repo.adauga(stud)

    def cauta_student(self, id):
        lista_studenti = self.__stud_repo.getclasa()
        for elem in lista_studenti:
            if elem.getID() == id:
                return elem
        return -1

    def cauta_student_recursiv(self, id, index):
        "cauta student dupa id recursiv"
        lista = self.get_studenti()
        if index <= len(lista) - 1:
            if lista[index].getID() == id:
                return lista[index]
            else:
                self.cauta_student_recursiv(id, index + 1)

    def genereaza_student(self):
        '''
        genereaza o entitate student si valideaza datele
        :return: student cu toate datele random
        '''
        caractere = string.ascii_lowercase
        nume = ''.join(random.choices(caractere + " ", k=13))
        caractere = string.digits
        grupa = ''.join(random.choices(caractere, k=3))
        id = ''.join(random.choices(caractere, k=5))
        s = student(id, 'nume', 213)
        while not self.__validator_student.valideaza_id(s, self.__stud_repo):
            s = student(''.join(random.choices(caractere, k=5)), 'nume', 213)
        self.creere_student(id, nume, grupa)

    def sterge_student(self, id):
        '''
        se scote o entitate student din lista din cadrul repo_student
        :param id: id dupa care se sterge studentul
        :return: o noua lista
        '''
        lista_studenti = self.__stud_repo.getclasa()
        for elem in lista_studenti:
            if elem.getID() == id:
                lista_studenti.remove(elem)
                break
        self.__stud_repo.actualizeaza(lista_studenti)

    def sterge_student_recursiv(self, id, index, lista):
        """
          se scote o entitate student din lista din cadrul repo_student recursiv
        :param id: id dupa care se cauta studentul pentru a se elimina
        :param index: studentul curent
        :param lista: lista in care se cauta
        :return: o lista actualizata
        """
        if index <= len(lista) - 1:
            if lista[index].getID() == id:
                lista.remove(lista[index])
                self.sterge_student_recursiv(id, len(lista), lista)
            else:
                self.sterge_student_recursiv(id, index + 1, lista)
        else:
            self.__stud_repo.actualizeaza(lista)

    def sorteaza_alfabetic(self):
        lista = self.get_studenti()
        n = len(lista)
        i = 0  # index
        while i < n - 1:
            j = i + 1
            while j < n:
                if lista[i].getnume() > lista[j].getnume():
                    x = lista[i]
                    lista[i] = lista[j]  # interschimbare
                    lista[j] = x
                j += 1
            i += 1
        return lista  # returneaza lista

    def get_student(self, index):
        return self.__stud_repo.getstudent_clasa(index)

    def get_studenti(self):
        return self.__stud_repo.getclasa()

    def afiseaza_studenti(self):
        clasa_fisier = fisier_studenti_repo("fisier_studenti")
        n = input("Alegeti 1 daca rezultatul sa se tipareasca pe ecran sau 2 daca in fisier ")
        if n == '1':
            self.__stud_repo.afiseaza()
        else:
            clasa_fisier.scrie_in_fisier_lista(self.__stud_repo.getclasa())

    def lista_studenti_fisier(self):
        clasa_fisier = fisier_studenti_repo("fisier_studenti")
        lista = clasa_fisier.load_from_file()
        self.__stud_repo.actualizeaza(lista)

    def afiseaza_fisier(self, elem):
        clasa_fisier = fisier_studenti_repo("fisier_studenti")
        clasa_fisier.scrie_in_fisier(elem)

    def adauga_student_fisier(self):
        fisier_student = fisier_studenti_repo("fisier_studenti")
        stud = fisier_student.citeste_student()
        self.__stud_repo.adauga(stud)
