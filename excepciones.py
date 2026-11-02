"""Excepciones del dominio académico para la Actividad Colaborativa N.º 2."""


class ErrorAcademico(Exception):
    """Clase base para situaciones de negocio del sistema académico."""


class EstudianteYaMatriculadoError(ErrorAcademico):
    """Se intentó registrar dos veces el mismo código estudiantil."""


class CupoAgotadoError(ErrorAcademico):
    """El grupo no dispone de plazas disponibles."""


class EstudianteNoMatriculadoError(ErrorAcademico):
    """El código solicitado no está matriculado en el grupo."""


class AsignaturaNoEncontradaError(ErrorAcademico):
    """No existe una asignatura con el código consultado."""


class ProgramaNoEncontradoError(ErrorAcademico):
    """No existe un programa académico con el código consultado."""
