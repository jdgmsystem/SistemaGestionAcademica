"""Catálogos y búsquedas del mismo Sistema de Gestión Académica."""

from modelos import Asignatura, ProgramaAcademico, _texto_obligatorio
from grupo_academico import GrupoAcademico
from excepciones import AsignaturaNoEncontradaError, ProgramaNoEncontradoError


class SistemaAcademico:
    """Coordina programas, asignaturas y grupos sin sustituir sus clases."""

    def __init__(self):
        self.__programas = {}
        self.__asignaturas = {}
        self.__grupos = {}

    def registrar_programa(self, programa):
        if not isinstance(programa, ProgramaAcademico):
            raise ValueError("Debe registrar un ProgramaAcademico válido.")
        if programa.codigo in self.__programas:
            raise ValueError(f"El programa {programa.codigo} ya está registrado.")
        self.__programas[programa.codigo] = programa

    def registrar_asignatura(self, asignatura):
        if not isinstance(asignatura, Asignatura):
            raise ValueError("Debe registrar una Asignatura válida.")
        if asignatura.codigo in self.__asignaturas:
            raise ValueError(f"La asignatura {asignatura.codigo} ya está registrada.")
        if asignatura.programa.codigo not in self.__programas:
            raise ValueError("El programa de la asignatura debe estar registrado.")
        self.__asignaturas[asignatura.codigo] = asignatura

    def registrar_grupo(self, grupo):
        if not isinstance(grupo, GrupoAcademico):
            raise ValueError("Debe registrar un GrupoAcademico válido.")
        if grupo.codigo in self.__grupos:
            raise ValueError(f"El grupo {grupo.codigo} ya está registrado.")
        if grupo.asignatura.codigo not in self.__asignaturas:
            raise ValueError("Primero debe registrarse la asignatura del grupo.")
        self.__grupos[grupo.codigo] = grupo

    def buscar_programa(self, codigo):
        codigo = _texto_obligatorio(codigo, "El código del programa")
        try:
            return self.__programas[codigo]
        except KeyError as exc:
            raise ProgramaNoEncontradoError(f"No existe el programa académico {codigo}.") from exc

    def buscar_asignatura(self, codigo):
        codigo = _texto_obligatorio(codigo, "El código de la asignatura")
        try:
            return self.__asignaturas[codigo]
        except KeyError as exc:
            raise AsignaturaNoEncontradaError(f"No existe la asignatura {codigo}.") from exc
