from Domain.entities import student, laborator, nota
from Domain.validatori import validator_student, validator_problema, validator_nota
from Repository.clasa_de_legatura_repo import clasa_de_legatura_repo
from Repository.probleme_repo import probleme_repo
from Repository.studenti_repo import test_clasa_adauga_student, studenti_repo
from Service.clasa_de_legatura_service import clasa_de_legatura_service
from Service.probleme_service import service_probleme
from Service.studenti_service import service_student
import unittest


class TestStudent(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_creere_student(self):
        id = 1234
        nume = "Marcel"
        grupa = 123
        rep = studenti_repo()
        serv = service_student(rep, validator_student())
        serv.creere_student(id, nume, grupa)
        f = serv.get_student(0)
        assert (f.getnume() == "Marcel")
        assert (f.getID() == 1234)
        assert (f.getgrup() == 123)

    def test_nota_adauga(self):
        '''
        testeaza functia adauga_nota din clasa note_repo
        :return: -
        '''
        s1 = student(12, "Marcel Mihai", 13)
        p1 = laborator("12_21", "Rezolva ex", "23/11/2021")
        n1 = nota(s1, p1, 2)
        n = clasa_de_legatura_repo()
        n.adauga_nota(n1)
        self.assertEqual(n.getnota(0), n1)

    def test_cauta_student(self):
        p = student("1234", "Marcel", "123")
        rep = studenti_repo()
        rep.adauga(p)
        val = None
        serv = service_student(rep, val)
        self.assertEqual(serv.cauta_student("1234"), p)
        self.assertEqual(serv.cauta_student("1321"), -1)

    def test_cauta_student_recursiv(self):
        p = student("1234", "Marcel", "123")
        rep = studenti_repo()
        rep.adauga(p)
        val = None
        serv = service_student(rep, val)
        self.assertEqual(serv.cauta_student_recursiv("1234", 0), p)
        self.assertEqual(serv.cauta_student_recursiv("1321", 0), None)

    def test_sterge_student(self):
        p = student("1234", "Marcel", "123")
        p1 = student("124", "Mihai", "123")
        rep = studenti_repo()
        rep.adauga(p)
        rep.adauga(p1)
        val = validator_student()
        serv = service_student(rep, val)
        serv.sterge_student("1234")
        lista = serv.get_studenti()
        self.assertEqual(lista[0].getID(), p1.getID())

    def test_sterge_student_recursiv(self):
        p = student("1234", "Marcel", "123")
        p1 = student("124", "Mihai", "123")
        rep = studenti_repo()
        rep.adauga(p)
        rep.adauga(p1)
        val = validator_student()
        serv = service_student(rep, val)
        serv.sterge_student_recursiv("1234", 0, serv.get_studenti())
        lista = serv.get_studenti()
        self.assertEqual(lista[0].getID(), p1.getID())

    def test_studenti_sub_5(self):
        s1 = student(" 55581", " qkzuyzeqnaefp", "854")
        s2 = student(" 34581", " qkzuyzefp", "54")
        p1 = laborator("23_86", "dnejfnkaga", "12/12/1345")
        n1 = nota(s1, p1, 1)
        n2 = nota(s1, p1, 5)
        n3 = nota(s2, p1, 9)
        r = clasa_de_legatura_repo()
        vs = validator_student()
        rs = studenti_repo()
        s = service_student(rs, vs)
        vp = validator_problema()
        pr = probleme_repo()
        p = service_probleme(vp, pr)
        v = validator_nota(s, p)
        note = clasa_de_legatura_service(v, r)
        note.adauga_nota(n1)
        note.adauga_nota(n2)
        note.adauga_nota(n3)
        lista = note.studenti_sub_5()
        self.assertEqual(lista[0], n1)

    def test_creere_nota(self):
        s1 = student("1234", "Marcel", "123")
        l = laborator("123_134", "suma", "12/12/2021")
        n = '5'
        n1 = nota(s1, l, n)

        stud_repo = studenti_repo()
        stud_repo.adauga(s1)
        stud_val = validator_student()
        stud = service_student(stud_repo, stud_val)

        lab_repo = probleme_repo()
        lab_repo.adauga(l)
        lab_val = validator_problema()
        lab = service_probleme(lab_repo, lab_val)

        v = validator_nota(stud, lab)
        repo = clasa_de_legatura_repo()
        ns = clasa_de_legatura_service(v, repo)

        ns.creere_nota(s1, l, n)
        self.assertEqual(ns.get_nota(0).get_nota(), n1.get_nota())

    def test_create_student(self):
        '''
        testeaza functia create student din cadrul clasei student
        :return:  -
        '''
        s1 = student(12, "Marcel Mihai", 13)
        self.assertEqual(s1.getID(), 12)
        self.assertEqual(s1.getnume(), "Marcel Mihai")
        self.assertEqual(s1.getgrup(), 13)

        s1.setID(1234)
        self.assertEqual(s1.getID(), 1234)
        s1.setnume("Popescu")
        self.assertEqual(s1.getnume(), "Popescu")
        s1.setgrup(12)
        self.assertEqual(s1.getgrup(), 12)

    def test_create_nota(self):
        '''
        testeaza functia create_nota din cadrul clasei nota
        :return: -
        '''
        s1 = student(12, "Marcel Mihai", 13)
        p1 = laborator("13_123", "Sa se calculeze suma", "12/12/2021")
        n1 = nota(s1, p1, 10)
        self.assertEqual(n1.get_nota(), 10)
        self.assertEqual(n1.get_student(), s1)
        self.assertEqual(n1.get_laborator(), p1)


class TestProbleme(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self):
        pass

    def test_create_problema(self):
        '''
        testeaza functia create_problema din cadrul clasei problema
        :return: -
        '''
        p1 = laborator("13_123", "Sa se calculeze suma", "12/12/2021")
        self.assertEqual(p1.getnumar_laborator_numar_problema(), "13_123")
        self.assertEqual(p1.getdescriere(), "Sa se calculeze suma")
        self.assertEqual(p1.getdeadline(), "12/12/2021")

        p1.setdeadline("31/02/2021")
        self.assertEqual(p1.getdeadline(), "31/02/2021")
        p1.setdescriere("rezolva exercitiu")
        self.assertEqual(p1.getdescriere(), "rezolva exercitiu")
        p1.setnumar_laborator_numar_problema("31_76")
        self.assertEqual(p1.getnumar_laborator_numar_problema(), "31_76")

    def test_adauga_probleme(self):
        p = laborator("12_21", "Rezolva ex", "23/11/2021")
        e = probleme_repo()
        e.adauga(p)
        self.assertEqual(e.getproblema_index(0), p)

    def test_cauta_problema(self):
        p = laborator("123_134", "suma", "12/12/2021")
        rep = probleme_repo()
        rep.adauga(p)
        val = None
        serv = service_probleme(rep, val)
        self.assertEqual(serv.cauta_problema("suma"), p)
        self.assertEqual(serv.cauta_problema("ceva"), -1)

    def test_creere_problema(self):
        nr = "12_65"
        descriere = "descriere"
        deadline = "12/12/1012"
        rep = probleme_repo()
        serv = service_probleme(rep, validator_problema())
        serv.creere_problema(nr, descriere, deadline)
        f = serv.getproblema(0)
        self.assertEqual(f.getnumar_laborator_numar_problema(), "12_65")
        self.assertEqual(f.getdescriere(), "descriere")
        self.assertEqual(f.getdeadline(), "12/12/1012")

    def test_sterge_problema(self):
        p = laborator("12_34", "descriere", "12/03/1231")
        p1 = laborator("12_4", "descriere2", "12/03/1234")
        rep = probleme_repo()
        rep.adauga(p)
        rep.adauga(p1)
        val = validator_problema()
        serv = service_probleme(rep, val)
        serv.sterge_problema("12_34")
        lista = serv.get_probleme()
        self.assertEqual(lista[0].getnumar_laborator_numar_problema(), p1.getnumar_laborator_numar_problema())


class test_clasa_de_legatura(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_creere_nota(self):
        s1 = student("1234", "Marcel", "123")
        l = laborator("123_134", "suma", "12/12/2021")
        n = '5'
        n1 = nota(s1, l, n)

        stud_repo = studenti_repo()
        stud_repo.adauga(s1)
        stud_val = validator_student()
        stud = service_student(stud_repo, stud_val)

        lab_repo = probleme_repo()
        lab_repo.adauga(l)
        lab_val = validator_problema()
        lab = service_probleme(lab_repo, lab_val)

        v = validator_nota(stud, lab)
        repo = clasa_de_legatura_repo()
        ns = clasa_de_legatura_service(v, repo)

        ns.creere_nota(s1, l, n)
        self.assertEqual(ns.get_nota(0).get_nota(), n1.get_nota())

    def test_create_nota(self):
        '''
        testeaza functia create_nota din cadrul clasei nota
        :return: -
        '''
        s1 = student(12, "Marcel Mhai", 13)
        p1 = laborator("13_123", "Sa se calculeze suma", "12/12/2021")
        n1 = nota(s1, p1, 10)
        self.assertEqual(n1.get_nota(), 10)
        self.assertEqual(n1.get_student(), s1)
        self.assertEqual(n1.get_laborator(), p1)
