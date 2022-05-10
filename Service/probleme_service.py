import random
import string

from Domain.entities import laborator
from Repository.probleme_repo import fisier_probleme_repo


class service_probleme:
    nr_probleme = 0

    def __init__(self, probleme_repo, validator_pb):
        self.__probleme_repo = probleme_repo
        self.__validator_problema = validator_pb

    def creere_problema(self, nr_prob, descriere, deadline):
        """
        creeaza o entitate problema din parametri dati si o adauga la lista probleme
        :param nr_prob: numarul problemei
        :param descriere: descrierea problemei
        :param deadline: deadlinul problemei
        :return: adauga parametrul in lista
        """
        p = laborator(nr_prob, descriere, deadline)
        if self.__validator_problema.numar_prob(p) and self.__validator_problema.deadline(p):
            service_probleme.nr_probleme += 1
            self.__probleme_repo.adauga(p)

    def cauta_problema(self, descriere):
        """
        Complexitate:
        Caz favorabil - cand primul element din lista este cel cautat - theta(1)
        Caz nefavorabil - ultimul element din lista e cel cautat - theta(n)
        Caz mediu - suma((1+2+...+n)/n) theta(n)
        Overall: O(n)
        """
        lista_probleme = self.__probleme_repo.getprobleme()
        for elem in lista_probleme:
            if elem.getdescriere() == descriere:
                return elem
        return -1

    def genereaza_problema(self):
        '''
        genereaza random si valideaza o entitate laborator
        :return: adauga o entitate laborator in probleme_repo
        '''
        caractere = string.ascii_lowercase
        descriere = ''.join(random.choices(caractere + " ", k=13))
        caractere = string.digits
        sep = "_"
        nr = [''.join(random.choices(caractere, k=3)), ''.join(random.choices(caractere, k=3))]
        nr = sep.join(nr)
        deadline = [str(random.randint(1, 31)), str(random.randint(1, 12)), str(random.randint(2007, 2022))]
        sep = "/"
        deadline = sep.join(deadline)
        self.creere_problema(nr, descriere, deadline)

    def sterge_problema(self, nr):
        lista_prob = self.__probleme_repo.getprobleme()
        for elem in lista_prob:
            if elem.getnumar_laborator_numar_problema() == nr:
                lista_prob.remove(elem)
        self.__probleme_repo.actualizeaza(lista_prob)

    def get_probleme(self):
        return self.__probleme_repo.getprobleme()

    def getproblema(self, index):
        return self.__probleme_repo.getproblema_index(index)

    def valideaza_nr(self, nr):
        self.__validator_problema.numar_prob(nr)

    def afiseaza_probleme(self):
        clasa_fisier = fisier_probleme_repo("fisier_lab")
        n = input("Alegeti 1 daca rezultatul sa se tipareasca pe ecran sau 2 daca in fisier ")
        if n == '1':
            self.__probleme_repo.afiseaza()
        else:
            clasa_fisier.scrie_in_fisier_lista(self.__probleme_repo.getprobleme())

    def lista_probleme_fisier(self):
        clasa_fisier = fisier_probleme_repo("fisier_lab")
        lista = clasa_fisier.load_from_file()
        self.__probleme_repo.actualizeaza(lista)

    def afiseaza_fisier(self, elem):
        clasa_fisier = fisier_probleme_repo("fisier_lab")
        clasa_fisier.scrie_in_fisier(elem)

    def adauga_problema_fisier(self):
        fisier_lab = fisier_probleme_repo("fisier_lab")
        stud = fisier_lab.citeste_problema()
        self.__probleme_repo.adauga(stud)

