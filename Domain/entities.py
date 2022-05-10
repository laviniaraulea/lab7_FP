class student:
    '''
    clasa student
    retine Id, numele si grupul
    '''

    def __init__(self, studentID, nume, grup):
        self.__studentID = studentID
        self.__nume = nume
        self.__grup = grup

    def getID(self):
        return self.__studentID

    def getnume(self):
        return self.__nume

    def getgrup(self):
        return self.__grup

    def setID(self, studentID):
        self.__studentID = studentID

    def setnume(self, nume):
        self.__nume = nume

    def setgrup(self, grup):
        self.__grup = grup

    def __str__(self):
        return "ID student: " + str(self.__studentID) + ' Nume student: ' + str(self.__nume) + ' Grup student: ' + str(
            self.__grup)

    def __getattr__(self, denumire):
        if denumire == 'ID':
            return self.__studentID
        elif denumire == 'nume':
            return self.__nume
        elif denumire == 'grup':
            return self.__grup



class laborator:
    '''
    clasa problema, retine numarul laboratorului, numarul problemei, descrierea laboratorului si deadline - ul la care trebuie predat
    '''

    def __init__(self, numar_laborator_numar_problema, descriere, deadline):
        self.__numar_laborator_numar_problema = numar_laborator_numar_problema
        self.__descriere = descriere
        self.__deadline = deadline

    def getnumar_laborator_numar_problema(self):
        return self.__numar_laborator_numar_problema

    def getdescriere(self):
        return self.__descriere

    def getdeadline(self):
        return self.__deadline

    def setnumar_laborator_numar_problema(self, numar_laborator):
        self.__numar_laborator_numar_problema = numar_laborator

    def setdescriere(self, descriere):
        self.__descriere = descriere

    def setdeadline(self, deadline):
        self.__deadline = deadline

    def __str__(self):
        return "Numar laborator si numar problema: " + str(self.__numar_laborator_numar_problema) + ' Descriere ' + str(
            self.__descriere) + " Deadline " + str(self.__deadline)

    def __getattr__(self, denumire):
        if denumire == 'numar':
            return self.__numar_laborator_numar_problema
        elif denumire == 'descriere':
            return self.__descriere
        elif denumire == 'deadline':
            return self.__deadline


class nota:
    '''
    Clasa nota
    retine studentul, laboratoru si nota
    '''

    def __init__(self, stud, lab, nota):
        self.__stud = stud
        self.__lab = lab
        self.__nota = nota

    def get_nota(self):
        return self.__nota

    def get_student(self):
        return self.__stud

    def get_laborator(self):
        return self.__lab

    def set_nota(self, nota):
        self.__nota = nota

    def set_student(self, stud):
        self.__stud = stud

    def set_lab(self, lab):
        self.__lab = lab

    def afiseaza(self):
        print(self)

    def __str__(self):
        return "Student: " + str(self.__stud.getID()) + ' Laborator: ' + str(
            self.__lab.getnumar_laborator_numar_problema()) + ' nota ' + str(
            self.__nota)

    def __getattr__(self, denumire):
        if denumire == 'student':
            return self.__stud
        elif denumire == 'laborator':
            return self.__lab
        elif denumire == 'nota':
            return self.__nota
