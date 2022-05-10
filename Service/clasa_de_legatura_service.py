from Domain.entities import nota, student, laborator
from Domain.validatori import validator_student, validator_nota, validator_problema
from Repository.clasa_de_legatura_repo import clasa_de_legatura_repo, fisier_clasa_de_legatura_repo
from Repository.probleme_repo import probleme_repo
from Repository.studenti_repo import studenti_repo, fisier_studenti_repo
from Service.probleme_service import service_probleme
from Service.studenti_service import service_student


class clasa_de_legatura_service:
    nr_note = 0

    def __init__(self, validator_note, n_repo):
        self.__validator = validator_note
        self.__note_repo = n_repo

    def adauga_nota(self, n):
        self.__note_repo.adauga_nota(n)

    def actualizeaza(self, lista):
        self.__note_repo.actualizeaza(lista)

    def creere_nota(self, stud, lab, n):
        n1 = nota(stud, lab, n)
        if self.__validator.valideaza_stud(n1) and self.__validator.nota(n1) and self.__validator.valideaza_prob(n1):
            self.__note_repo.adauga_nota(n1)
            clasa_de_legatura_service.nr_note += 1

    def get_nota(self, index):
        return self.__note_repo.getnota(index)

    def get_note(self):
        return self.__note_repo.getnote()

    def get_note_student(self, stud):
        lista = self.__note_repo.getnote()
        lista_note = []
        for elem in lista:
            if elem.get_student() == stud:
                lista_note.append(elem)
        return lista_note

    def sorteaza_note(self):
        '''
        sorteaza asignarile dupa note
        :return: lista ordonata
        '''
        lista = self.__note_repo.getnote()
        n = len(lista)
        i = 0
        while i < n - 1:
            j = i + 1
            while j < n:
                if lista[i].get_nota() < lista[j].get_nota():
                    x = lista[i]
                    lista[i] = lista[j]
                    lista[j] = x
                j += 1
            i += 1
        return lista

    def studenti_sub_5(self):
        '''
        creeaza o lista cu stiudentii care au media laboratorului sub 5
        :return: lista continand doar studenti sub 5
        '''
        lista = self.__note_repo.getnote()
        lista_finala = []
        n = len(lista)
        i = 0
        while i < n:
            nr_note = 1
            suma = int(lista[i].get_nota())
            j = i + 1
            while j < n:
                if lista[i].get_student() == lista[j].get_student():
                    suma += int(lista[j].get_nota())
                    nr_note += 1
                    lista.remove(lista[j])
                    n -= 1
                    j -= 1
                j += 1
            if suma / nr_note < 5:
                lista_finala.append(lista[i])

            i += 1
        return lista_finala

    def cele_mai_asignate_laboratoare(self):
        '''
        creeaza o lista cu cele mai asignate 3 laboratoare
        :return: lista cu 3 elemente
        '''
        lista = self.__note_repo.getnote()
        lista_finala = [0, 0, 0]
        n = len(lista)
        i = 0
        mx_1 = 0  # maximul de aparitii a 3 entitatu
        mx_2 = 0
        mx_3 = 0
        while i < n:
            nr_lab = 1
            lab = lista[i].get_laborator()
            j = i + 1
            while j < n:
                if lista[j].get_nota() != 0 and lab == lista[
                    j].get_laborator():  # lista[j].get_nota() != 0 ==> laboratorul nu e asignat inca
                    lista.remove(lista[j])
                    j -= 1
                    n -= 1
                    nr_lab += 1
                j += 1
            if nr_lab > mx_3:
                if nr_lab > mx_2:
                    if nr_lab > mx_1:
                        mx_3 = mx_2
                        mx_2 = mx_1
                        mx_1 = nr_lab
                        lista_finala[2] = lista_finala[
                            1]  # modifica ordinea in lista finala pentru a le afisa descrescator
                        lista_finala[1] = lista_finala[0]
                        lista_finala[0] = lab
                    else:
                        mx_3 = mx_2
                        mx_2 = nr_lab
                        lista_finala[2] = lista_finala[
                            1]  # modifica ordinea in lista finala pentru a le afisa descrescator
                        lista_finala[1] = lab
                else:
                    mx_3 = nr_lab
                    lista_finala[2] = lab  # modifica ordinea in lista finala pentru a le afisa descrescator
            i += 1
        return lista_finala

    def afiseaza_nota(self, index):
        self.__note_repo.afiseaza_nota(index)

    def afiseaza_note(self):
        self.__note_repo.afiseaza()

    def afiseaza_probleme(self):
        clasa_fisier = fisier_clasa_de_legatura_repo("fisier_asignare")
        n = input("Alegeti 1 daca rezultatul sa se tipareasca pe ecran sau 2 daca in fisier ")
        if n == '1':
            self.__note_repo.afiseaza()
        else:
            clasa_fisier.scrie_in_fisier_lista(self.__note_repo.getnote())

    def lista_probleme_fisier(self):
        clasa_fisier = fisier_clasa_de_legatura_repo("fisier_asignare")
        lista = clasa_fisier.load_from_file()
        self.__note_repo.actualizeaza(lista)

    def afiseaza_fisier(self, elem):
        clasa_fisier = fisier_clasa_de_legatura_repo("fisier_asignare")
        clasa_fisier.scrie_in_fisier(elem)

    def adauga_problema_fisier(self):
        fisier_lab = fisier_clasa_de_legatura_repo("fisier_asignare")
        nota = fisier_lab.citeste_nota()
        self.__note_repo.adauga(nota)
