#A) Paciente
from dataclasses import dataclasses

@dataclasses(frozen=True)
class Paciente:
    nome: str
    cartao_sus: str

#B) Atendimento, duracao_minutos, consulta, exame, vacinacao
class Consulta(Atendimento):
    def __init__(self, paciente: Paciente, especialidade: str, retorno: bool = False) -> None:
        super().__init__(paciente) # Passa o paciente pra mãe
        self.especialidade = especialidade
        self.retorno = retorno

    def duracao_minutos(self) -> int:
        return 15 if self.retorno else 30

class Exame(Atendimento):
    def __init__(self, paciente: Paciente, tipo: str, jejum: bool = False) -> None:
        super().__init__(paciente)
        self.tipo = tipo
        self.jejum = jejum

    def duracao_minutos(self) -> int:
        return 30 if self.jejum else 20

class Vacinacao(Atendimento):
    def __init__(self, paciente: Paciente, vacina: str, doses: int = 1) -> None:
        super().__init__(paciente)
        self.vacina = vacina
        self.doses = doses

    def duracao_minutos(self) -> int:
        return 10 * self.doses

#C) Execeções personalizadas
class AgendaError(Exception):
    """Erro base da nossa aplicação."""
    pass

class HorarioIndisponivelError(AgendaError):
    """Erro para quando o tempo estourar o limite."""
    pass

class PacienteJaAgendadoError(AgendaError):
    """Erro para quando o paciente já está na lista."""
    pass

#D) Agenda
class Agenda:
    def __init__(self, limite_minutos: int = 240) -> None:
        self.limite_minutos = limite_minutos
        self.atendimentos: list[Atendimento] = []

    @property
    def minutos_ocupados(self) -> int:
        return 

#E) Nomenclatura e tipagem.
