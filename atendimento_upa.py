#A) Paciente
from dataclasses import dataclasses

@dataclasses(frozen=True)
class Paciente:
    nome: str
    cartao_sus: str

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


#E) Nomenclatura e tipagem.
