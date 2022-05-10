from random import randint

from termcolor import colored


class console:
    def __init__(self, stud_service, prob_service, nota_service):
        self.__stud_service = stud_service
        self.__prob_service = prob_service
        self.__nota_service = nota_service

    @staticmethod
    def print_meniu():
        print(colored("Adauga student, laborator, nota", 'green'))
        print(colored("Citeste studenti din fisier", 'green'))
        print(colored("Cauta problema dupa descriere", 'green'))
        print(colored("Cauta student dupa id", 'green'))
        print(colored("Stergere student, problema", 'green'))
        print(colored("Afiseaza studenti alfabetic", 'green'))
        print(colored("Afiseaza studenti sub 5", 'green'))
        print(colored("Sortare note", 'green'))
        print(colored("Asignare laborator", 'green'))
        print(colored("Afiseaza asignare", 'green'))
        print(colored("Afiseaza cele mai asignate laburi", 'green'))
        print(colored("Iesire", 'green'))

    def afiseaza_studenti(self):
        self.__stud_service.afiseaza_studenti()

    def afiseaza_probleme(self):
        self.__prob_service.afiseaza_probleme()

    def afiseaza_asignare(self):
        self.__nota_service.afiseaza_note()

    def studenti_fisier(self):
        self.__stud_service.lista_studenti_fisier()

    def adauga_student_fisier(self):
        self.__stud_service.adauga_student_fisier()

    def adauga_problema_fisier(self):
        self.__prob_service.adauga_problema_fisier()

    def probleme_fisier(self):
        self.__prob_service.lista_probleme_fisier()

    def asignare_fisier(self):
        self.__nota_service.lista_probleme_fisier()

    def adauga_student(self):
        id = input("Id studentului este: ")
        nume = input("Numele studentului este ")
        grupa = input("Grupa este ")
        self.__stud_service.creere_student(id, nume, grupa)

    def adauga_problema(self):
        nr = input("Numaul problemei si al laboratorului (ex.12_535) ")
        descriere = input("Descrierea problemei ")
        deadline = input("Deadlinul este ")
        self.__prob_service.creere_problema(nr, descriere, deadline)

    def adauga_nota(self):
        self.afiseaza_studenti()
        self.afiseaza_probleme()
        id = input("Id studentului caruia sa ii se adauge nota ")
        descriere = input("Descrierea laboratorului ")
        n = input("Nota ")
        stud = self.__stud_service.cauta_student(id)
        prob = self.__prob_service.cauta_problema(descriere)
        if stud != -1 and prob != -1:
            self.__nota_service.creere_nota(stud, prob, n)
        else:
            print(colored("Studentul sau problema nu exista", 'red'))

    def asignare_lab(self):
        self.afiseaza_studenti()
        self.afiseaza_probleme()
        id = input("Id studentului caruia sa ii se adauge nota ")
        descriere = input("Descrierea laboratorului ")
        n = 0
        stud = self.__stud_service.cauta_student(id)
        prob = self.__prob_service.cauta_problema(descriere)
        if stud != -1 and prob != -1:
            self.__nota_service.creere_nota(stud, prob, n)
        else:
            print(colored("Studentul sau problema nu exista", 'red'))

    def cauta_problema(self):
        descriere = input("Descrierea dupa care sa se caute problema este ")
        prob = self.__prob_service.cauta_problema(descriere)
        if prob == -1:
            print(colored("Problema nu a fost gasita", 'red'))
        else:
            n = input("1 pentru consola, 2 pentru fisier ")
            if n == 1:
                print("Problema este " + prob.getnumar_laborator_numar_problema())
            else:
                self.__prob_service.afiseaza_probleme_fisier(prob.getnumar_laborator_numar_problema())

    def cauta_student(self):
        id = input("Id dupa care sa se caute sudentul ")
        stud = self.__stud_service.cauta_student(id)
        if stud == -1:
            print(colored("Studentul nu a fost gasit", 'red'))
        else:
            n = input("Alegeti 1 daca rezultatul sa se tipareasca pe ecran sau 2 daca in fisier ")
            if n == '1':
                print("Studentul este " + stud.getnume())
            else:
                self.__stud_service.afiseaza_fisier(stud.getnume())

    def sterge_student(self):
        id = input("Id dupa care sa se sterga sudentul ")
        self.__stud_service.sterge_student(id)
        self.__stud_service.afiseaza_studenti()

    def stergere_problema(self):
        nr = input("Nr dupa care sa se sterga problema ")
        self.__prob_service.sterge_problema(nr)
        self.__prob_service.afiseaza_probleme()

    def genereaza_student(self):
        self.__stud_service.genereaza_student()
        print(colored("Entitatea a fost generata", 'cyan'))

    def genereaza_problema(self):
        self.__prob_service.genereaza_problema()
        print(colored("Entitatea a fost generata", 'cyan'))

    def sortare_studenti_alfabetic(self):
        self.__stud_service.actualizeaza(self.__stud_service.sorteaza_alfabetic())
        self.__stud_service.afiseaza_studenti()

    def sortare_studenti_note(self):
        self.__nota_service.actualizeaza(self.__nota_service.sorteaza_note())
        self.__nota_service.afiseaza_note()

    def genereaza_nota(self):
        lista = self.__stud_service.get_studenti()
        n = len(lista)
        i = randint(0, n - 1)
        lista1 = self.__prob_service.get_probleme()
        n = len(lista1)
        j = randint(0, n - 1)
        self.__nota_service.creere_nota(lista[i], lista1[j], randint(1, 10))

    def studenti_sub_5(self):
        l = self.__nota_service.studenti_sub_5()
        n = input("1 pentru consola, 2 pentru fisier")
        if n == "1":
            for i in range(len(l)):
                print(l[i].get_student())
        else:
            for i in range(len(l)):
                self.__stud_service.afiseaza_fisier(l[i].get_student)

    def cele_mai_asignate_laburi(self):
        l = self.__nota_service.cele_mai_asignate_laboratoare()
        n = input("1 pentru consola, 2 pentru fisier")
        if n == '1':
            for i in range(len(l)):
                if l[i] != 0:
                    print(l[i])
        else:
            for i in range(len(l)):
                if l[i] != 0:
                    self.__prob_service.lista_probleme_fisier(l[i])

    def meniu(self):
        while True:
            self.print_meniu()
            cmd = input("Alege comanda ")
            if cmd == "adauga student":
                self.adauga_student()
            elif cmd == "adauga student fisier":
                self.adauga_student_fisier()
            elif cmd == "adauga laborator fisier":
                self.adauga_problema_fisier()
            elif cmd == "adauga asignari":
                self.asignare_fisier()
            elif cmd == "adauga studenti":
                self.studenti_fisier()
            elif cmd == "adauga laboratoare":
                self.probleme_fisier()
            elif cmd == "adauga laborator":
                self.adauga_problema()
            elif cmd == "cauta laborator":
                self.cauta_problema()
            elif cmd == "cauta student":
                self.cauta_student()
            elif cmd == "stergere student":
                self.sterge_student()
            elif cmd == "stergere laborator":
                self.stergere_problema()
            elif cmd == "afiseaza studenti":
                self.afiseaza_studenti()
            elif cmd == "afiseaza laborator":
                self.afiseaza_probleme()
            elif cmd == "genereaza student":
                self.genereaza_student()
            elif cmd == "genereaza laborator":
                self.genereaza_problema()
            elif cmd == "adauga nota":
                self.adauga_nota()
            elif cmd == "sortare alfabetic":
                self.sortare_studenti_alfabetic()
            elif cmd == "sortare dupa note":
                self.sortare_studenti_note()
            elif cmd == "genereaza nota":
                self.genereaza_nota()
            elif cmd == "asignare laborator":
                self.asignare_lab()
            elif cmd == "afiseaza asignare":
                self.afiseaza_asignare()
            elif cmd == "studenti sub 5":
                self.studenti_sub_5()
            elif cmd == "cele mai asignate laburi":
                self.cele_mai_asignate_laburi()
            else:
                print(colored("Optiune invalida", 'red'))
