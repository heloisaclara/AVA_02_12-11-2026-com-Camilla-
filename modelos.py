from abc import ABC, abstractmethod
from dataclasses import dataclass
from excecoes import HorarioIndisponivelError, PacienteJaAgendadoError


#A) Paciente
@dataclass(frozen=True)
class Paciente:
    nome: str
    cartao_sus: str

#B) Atendimento, duracao_minutos, consulta, exame, vacinacao
class Atendimento(ABC):
    def __init__(self, paciente: Paciente) -> None:
        self._paciente: Paciente = paciente

    @property
    def paciente(self) -> Paciente:
        return self._paciente

    @abstractmethod
    def duracao_minutos(self) -> int:
        pass

    def __str__(self) -> str:
        tipo = type(self).__name__
        duracao = self.duracao_minutos()
        return f"{tipo} - Paciente: {self._paciente.nome} - Duração: {duracao} min."

class Consulta(Atendimento):
    def __init__(self, paciente: Paciente, especialidade: str, retorno: bool = False) -> None:
        super().__init__(paciente)
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

#D) Agenda
class Agenda:
    def __init__(self, limite_minutos: int = 240) -> None:
        self.limite_minutos = limite_minutos
        self._atendimentos: list[Atendimento] = []

    @property
    def atendimentos(self) -> tuple[Atendimento, ...]:
        return tuple(self._atendimentos)

    @property
    def minutos_ocupados(self) -> int:
        return sum(atendimento.duracao_minutos() for atendimento in self._atendimentos)

    def agendar(self, atendimento: Atendimento) -> None:
        for ja_agendado in self._atendimentos:
            if ja_agendado.paciente == atendimento.paciente:
                raise PacienteJaAgendadoError(f"O paciente {atendimento.paciente.nome} já possui um atendimento agendado.")
    
        duracao = atendimento.duracao_minutos()
        if self.minutos_ocupados + duracao > self.limite_minutos:
            minutos_restantes = self.limite_minutos - self.minutos_ocupados
            raise HorarioIndisponivelError(f"Horário indisponível. Necessário {duracao} min, restam apenas {max(0, minutos_restantes)} min.")
        
        self._atendimentos.append(atendimento)