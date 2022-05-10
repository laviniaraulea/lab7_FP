from termcolor import colored


class validator_problema:
    def numar_prob(self, problema):
        if problema.getnumar_laborator_numar_problema().find("_") == -1:
            print(colored("Introduceti numar laboratorului si numarul problemei in formatul nr_nr", 'red'))
            return False
        numar = problema.getnumar_laborator_numar_problema().split("_")
        try:
            numar[0] = int(numar[0])
            numar[1] = int(numar[1])
        except ValueError:
            print(colored("Introduceti numar laboratorului si numarul problemei in formatul nr_nr", 'red'))
            return False
        return True

    def deadline(self, problema):
        deadline = problema.getdeadline().split("/")
        try:
            deadline[0] = int(deadline[0])
            deadline[1] = int(deadline[1])
            deadline[2] = int(deadline[2])
            if deadline[0] > 31:
                print(colored("Introduceti deadline de formatul dd/mm/yyyy", 'red'))
                return False
            if deadline[1] > 12:
                print(colored("Introduceti deadline de formatul dd/mm/yyyy", 'red'))
                return False
        except ValueError:
            print(colored("Introduceti deadline de formatul dd/mm/yyyy", 'red'))
        return True


class validator_student:
    def valideaza_id(self, stud, studenti_repo):
        lista_studenti = studenti_repo.getclasa()
        id = stud.getID()
        try:
            id = int(id)
        except ValueError:
            print(colored("Introduceti un numar pt ID", 'red'))
        for elem in lista_studenti:
            if id == elem.getID():
                print(colored("Introduceti un ID unic", 'red'))
                return False
        return True

    def valideaza_nume(self, stud):
        if stud.getnume().isdigit():
            print(colored("Numele nu trebuie sa contina numere", 'red'))
            return False
        return True

    def valideaza_grupa(self, stud):
        grupa = stud.getgrup()
        try:
            grupa = int(grupa)
        except ValueError:
            print(colored("Introduceti un numar pentru grupa", 'red'))
            return False
        return True


class validator_nota:
    def __init__(self, stud_serv, prob_serv):
        self.__stud_serv = stud_serv
        self.__prob_serv = prob_serv

    def nota(self, nota):
        try:
            n = int(nota.get_nota())
            if n > 10 and n < 1:
                return False
        except ValueError:
            print(colored("Introduceti un numar intre 1 si 10 pentru nota", 'red'))
            return False
        return True

    def valideaza_stud(self, nota):
        if self.__stud_serv.cauta_student(nota.get_student().getID()) != -1:
            return True
        return False

    def valideaza_prob(self, nota):
        if self.__prob_serv.cauta_problema(nota.get_laborator().getdescriere()) != -1:
            return True
        return False
