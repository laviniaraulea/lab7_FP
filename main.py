from Domain.validatori import validator_student, validator_problema, validator_nota
from Repository.probleme_repo import probleme_repo
from Repository.studenti_repo import studenti_repo
from Service.probleme_service import service_probleme
from Service.studenti_service import service_student
from Service.clasa_de_legatura_service import clasa_de_legatura_service
from Repository.clasa_de_legatura_repo import clasa_de_legatura_repo
from UI.console import console

stud_repo = studenti_repo()
stud_val = validator_student()
stud = service_student(stud_repo, stud_val)
lab_repo = probleme_repo()
lab_val = validator_problema()
lab = service_probleme(lab_repo, lab_val)
note_repo = clasa_de_legatura_repo()
note_val = validator_nota(stud, lab)
note = clasa_de_legatura_service(note_val, note_repo)
ui = console(stud, lab, note)
ui.meniu()
