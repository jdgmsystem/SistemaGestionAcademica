"""Oferta académica: clases Horario y GrupoAcademico.

La relación GrupoAcademico-Horario es composición: el grupo construye su
propio Horario dentro de __init__ y lo conserva como atributo privado.
"""

from datetime import datetime

from modelos import Asignatura, Docente, Estudiante, _entero_positivo, _texto_obligatorio
from excepciones import (
    CupoAgotadoError,
    EstudianteNoMatriculadoError,
    EstudianteYaMatriculadoError,
)


class Horario:
    """Valor de horario asociado a un grupo; incluye día, horas y salón."""

    def __init__(self, dia, hora_inicio, hora_fin, salon):
        self.__dia = _texto_obligatorio(dia, "El día")
        self.__salon = _texto_obligatorio(salon, "El salón")
        self.__hora_inicio = self._convertir_hora(hora_inicio, "inicio")
        self.__hora_fin = self._convertir_hora(hora_fin, "finalización")
        if self.__hora_fin <= self.__hora_inicio:
            raise ValueError("La hora de finalización debe ser posterior a la hora de inicio.")

    @staticmethod
    def _convertir_hora(valor, campo):
        if not isinstance(valor, str):
            raise ValueError(f"La hora de {campo} debe expresarse como HH:MM.")
        try:
            hora = datetime.strptime(valor, "%H:%M").time()
        except ValueError as exc:
            raise ValueError(f"La hora de {campo} debe expresarse como HH:MM válido.") from exc
        return hora

    @property
    def dia(self):
        return self.__dia

    @property
    def hora_inicio(self):
        return self.__hora_inicio.strftime("%H:%M")

    @property
    def hora_fin(self):
        return self.__hora_fin.strftime("%H:%M")

    @property
    def salon(self):
        return self.__salon

    def mostrar_informacion(self):
        return f"{self.dia}, {self.hora_inicio} a {self.hora_fin}, salón {self.salon}"


class GrupoAcademico:
    """Asocia objetos existentes de Asignatura y Docente con estudiantes.

    Al recibir datos elementales del horario, construye internamente su
    propio objeto Horario. Se evita guardar códigos/nombres en lugar de
    objetos y se protege la lista de matrículas contra edición externa.
    """

    def __init__(self, codigo, asignatura, docente, capacidad_maxima,
                 dia, hora_inicio, hora_fin, salon):
        self.__codigo = _texto_obligatorio(codigo, "El código del grupo")
        if not isinstance(asignatura, Asignatura):
            raise ValueError("El grupo requiere un objeto Asignatura válido.")
        if not isinstance(docente, Docente):
            raise ValueError("El grupo requiere un objeto Docente válido.")
        self.__asignatura = asignatura
        self.__docente = docente
        self.__capacidad_maxima = _entero_positivo(capacidad_maxima, "La capacidad máxima")
        self.__estudiantes = []
        # Composición: Horario se crea como parte del grupo, no se hereda.
        self.__horario = Horario(dia, hora_inicio, hora_fin, salon)

    @property
    def codigo(self):
        return self.__codigo

    @property
    def asignatura(self):
        return self.__asignatura

    @property
    def docente(self):
        return self.__docente

    @property
    def horario(self):
        return self.__horario

    @property
    def capacidad_maxima(self):
        return self.__capacidad_maxima

    @property
    def estudiantes(self):
        """Devuelve una vista inmutable; los cambios pasan por métodos."""
        return tuple(self.__estudiantes)

    def matricular_estudiante(self, estudiante):
        """Añade a un estudiante o lanza una excepción académica concreta."""
        if not isinstance(estudiante, Estudiante):
            raise ValueError("Se requiere un objeto Estudiante válido para matricular.")
        if any(e.codigo_estudiantil == estudiante.codigo_estudiantil for e in self.__estudiantes):
            raise EstudianteYaMatriculadoError(
                f"El estudiante {estudiante.codigo_estudiantil} ya está matriculado en {self.codigo}.")
        if len(self.__estudiantes) >= self.__capacidad_maxima:
            raise CupoAgotadoError(f"El grupo {self.codigo} alcanzó su capacidad máxima.")
        self.__estudiantes.append(estudiante)
        return f"Matrícula realizada: {estudiante.nombre} en grupo {self.codigo}."

    def retirar_estudiante(self, codigo_estudiantil):
        codigo = _texto_obligatorio(codigo_estudiantil, "El código estudiantil")
        for i, estudiante in enumerate(self.__estudiantes):
            if estudiante.codigo_estudiantil == codigo:
                self.__estudiantes.pop(i)
                return f"Retiro realizado: {codigo} del grupo {self.codigo}."
        raise EstudianteNoMatriculadoError(
            f"El estudiante {codigo} no está matriculado en {self.codigo}.")

    def mostrar_estudiantes(self):
        if not self.__estudiantes:
            return f"Grupo {self.codigo}: sin estudiantes matriculados."
        return "\n".join(
            f"- {estudiante.codigo_estudiantil}: {estudiante.nombre}"
            for estudiante in self.__estudiantes
        )

    def mostrar_informacion_grupo(self):
        return (f"Grupo: {self.codigo}\n"
                f"Asignatura: {self.asignatura.nombre} ({self.asignatura.codigo})\n"
                f"Docente: {self.docente.nombre}\n"
                f"Capacidad máxima: {self.capacidad_maxima}\n"
                f"Matriculados: {len(self.__estudiantes)}\n"
                f"Horario: {self.horario.mostrar_informacion()}")
