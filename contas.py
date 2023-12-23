from rich_menu import Menu

def menu():
    menu = Menu(
        "CRA",
        "MGA",
        color="bold purple",
        rule_title="calculadora de rendimento",
        align="center",
        panel_title="escolha a modalidade",
        selection_char="->",
    )
    selected = menu.ask(screen=False)
    return selected

def semestres():
    semestres = Menu(
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
        color="bold purple",
        rule_title="semestre",
        align="center",
        panel_title="selecione quantos semestres entrarão no cálculo",
        selection_char="->",
    )
    selected = semestres.ask(screen=False)
    return selected
def curso():
    curso = Menu(
        "até 2400 horas",
        "entre 2400 e 3600 horas",
        "mais de 3600 horas",
        color="bold purple",
        rule_title="carga horária total do curso",
        panel_title="selecione em qual categoria você se encaixa",
        selection_char="->",
    )
    selected = curso.ask(screen=False)
    return selected
def cra(result_curso):
    matriculas_do_semestre = int(input("Quantas matérias você se matriculou no semestre? "))

    trancamento = int(input("Digite a quantidade de matérias com trancamento parcial: ")) - 1
    if result_curso == "até 2400 horas":
        if trancamento <=4:
            trancamento = -1
        else: trancamento = trancamento - 4
    if result_curso == "entre 2400 e 3600 horas":
        if trancamento <=5:
            trancamento = -1
        else: trancamento = trancamento - 5
    if result_curso == "mais de 3600 horas":
        if trancamento <= 6:
            trancamento = -1
        else: trancamento = trancamento - 6

    carga_horaria_matriculada = 0
    for _ in range(trancamento + 1):
        carga_t = int(input("Digite a carga horária dos componentes curriculares com trancamento parcial: "))
        carga_horaria_matriculada += carga_t

    reprovacao_faltas = int(input("Digite a quantidade de reprovação por faltas: ")) - 1
    carga_horaria_reprovacao_falta = 0
    for _ in range(reprovacao_faltas + 1):
        carga_r = int(input("Digite a carga horária dos componentes curriculares em que houve reprovação por faltas: "))
        carga_horaria_reprovacao_falta += carga_r

    matricula_basica = matriculas_do_semestre - (trancamento + 1) - (reprovacao_faltas + 1)
    
    numerador1 = 0
    carga_horaria_cursada = 0
    for _ in range(matricula_basica):
        carga, nota = input("Digite a carga horária e a nota das matérias em que não houve trancamento, nem reprovação por falta (ex: 90 78): ").split()
        carga_horaria_cursada += int(carga)
        numerador1 += int(nota) * int(carga)
    
    carga_horaria_matriculada += carga_horaria_cursada
    
    if carga_horaria_reprovacao_falta == 0:
        cra = numerador1 / carga_horaria_matriculada
    else:
        cra = (numerador1 / carga_horaria_matriculada) * (carga_horaria_reprovacao_falta / (2 * carga_horaria_matriculada))
    return cra

def mga():
    materias_matriculadas = int(input("Digite a quantidade de matérias cursadas: "))
    produto = 0
    carga_ = 0
    for _ in range(materias_matriculadas):
        carga, nota = input("Digite a carga horária e a nota da matéria: ").split()
        produto += int(nota) * int(carga)
        carga_ += int(carga)
    mga = produto / carga_
    return mga

def main():
    result_curso = curso()
    selected_semesters = semestres()  
    if menu() == "CRA":
        total_cra = 0 
        for _ in range(int(selected_semesters)):
            total_cra += cra(result_curso)

        average_cra = total_cra / int(selected_semesters)
        print(f"Média de CRA de {selected_semesters} semestres: {average_cra}")
    else:
        mga_result = mga()
        print(f"MGA: {mga_result}")
main()