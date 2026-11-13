from modelos import Agenda, Paciente, Consulta, Exame, Vacinacao
from excecoes import AgendaError

def main() -> None:
    print("=== Iniciando a Agenda da UPA ===")

    agenda = Agenda() #criando agenda

    #criando pacientes
    p1 = Paciente("Ana Ferreira", 800000001)
    p2 = Paciente("José Sousa", 800000002)
    p3 = Paciente("Maria Lima", 800000003)

    #cadastrando atendimentos
    try:
        atend1 = Consulta(p1, "Clinica Geral")
        atend2 = Exame(p2, "Glicemia", jejum=True)
        atend3 = Vacinacao(p3, "Influenza", doses=2)

        agenda.agendar(atend1)
        agenda.agendar(atend2)
        agenda.agendar(atend3)

        print("\nAtendimentos cadastrados com sucesso!")
        print(f"Minutos ocupados na agenda: {agenda.minutos_ocupados} min")

        print("\nLista de atendimento na agenda:")
        for atendimento in agenda.atendimentos:
            print(f"- {atendimento}")            

    except AgendaError as erro:
        print(f"Erro na agenda: {erro}") 

if __name__ == "__main__":
    main()