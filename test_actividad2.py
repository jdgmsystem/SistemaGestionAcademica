"""Pruebas de la Actividad Colaborativa N.º 2 y regresión de POO."""

import inspect
import unittest

from modelos import Administrativo, Asignatura, Docente, Estudiante, Persona, ProgramaAcademico
from grupo_academico import GrupoAcademico, Horario
from sistema_academico import SistemaAcademico
from excepciones import (
    AsignaturaNoEncontradaError, CupoAgotadoError,
    EstudianteNoMatriculadoError, EstudianteYaMatriculadoError,
    ProgramaNoEncontradoError,
)


class PruebasActividad2(unittest.TestCase):
    def setUp(self):
        self.programa = ProgramaAcademico("IS", "Ingeniería de Sistemas", "Ingenierías", 10)
        self.asignatura = Asignatura("POO", "Programación POO", 3, self.programa)
        self.docente = Docente("200", "Marta", "m@u.edu", "D200", "Ingenierías", "Planta", 40)
        self.est1 = Estudiante("101", "Ana", "ana@u.edu", "E001", self.programa, 3, 4.3)
        self.est2 = Estudiante("102", "Pablo", "p@u.edu", "E002", self.programa, 2, 4.1)
        self.est3 = Estudiante("103", "Laura", "l@u.edu", "E003", self.programa, 4, 4.5)
        self.grupo = GrupoAcademico("POO-A", self.asignatura, self.docente, 2,
                                    "Lunes", "08:00", "10:00", "A-201")
        self.sistema = SistemaAcademico()
        self.sistema.registrar_programa(self.programa)
        self.sistema.registrar_asignatura(self.asignatura)
        self.sistema.registrar_grupo(self.grupo)

    def test_persona_abstracta_no_se_instancia(self):
        self.assertTrue(inspect.isabstract(Persona))
        with self.assertRaises(TypeError):
            Persona("1", "Nombre", "n@u.edu")

    def test_subclases_implementan_metodo_abstracto(self):
        adm = Administrativo("301", "Rosa", "r@u.edu", "A1", "Registro", "Auxiliar", "Diurna")
        for persona in (self.est1, self.docente, adm):
            self.assertIsInstance(persona, Persona)
            self.assertIsInstance(persona.realizar_actividad_principal(), str)
            self.assertTrue(persona.realizar_actividad_principal())

    def test_grupo_tiene_referencias_a_objetos_originales(self):
        self.assertIs(self.grupo.asignatura, self.asignatura)
        self.assertIs(self.grupo.docente, self.docente)
        self.assertIn("Programación POO", self.grupo.mostrar_informacion_grupo())

    def test_composicion_horario(self):
        self.assertIsInstance(self.grupo.horario, Horario)
        self.assertEqual(self.grupo.horario.dia, "Lunes")
        self.assertEqual(self.grupo.horario.salon, "A-201")
        self.assertIn("08:00", self.grupo.horario.mostrar_informacion())

    def test_dos_grupos_para_una_asignatura(self):
        otro = GrupoAcademico("POO-B", self.asignatura, self.docente, 1,
                              "Martes", "09:00", "11:00", "B-202")
        self.assertIs(otro.asignatura, self.grupo.asignatura)
        self.assertIsNot(otro.horario, self.grupo.horario)
        self.assertNotEqual(otro.horario.dia, self.grupo.horario.dia)

    def test_matricula_valida_y_consulta(self):
        self.grupo.matricular_estudiante(self.est1)
        self.assertEqual(len(self.grupo.estudiantes), 1)
        self.assertIs(self.grupo.estudiantes[0], self.est1)
        self.assertIn("E001: Ana", self.grupo.mostrar_estudiantes())

    def test_matricula_duplicada_mismo_codigo(self):
        self.grupo.matricular_estudiante(self.est1)
        est_clon = Estudiante("999", "Ana nueva", "an@u.edu", "E001", self.programa, 3, 4.0)
        with self.assertRaises(EstudianteYaMatriculadoError):
            self.grupo.matricular_estudiante(est_clon)
        self.assertEqual(len(self.grupo.estudiantes), 1)

    def test_cupo_agotado(self):
        self.grupo.matricular_estudiante(self.est1)
        self.grupo.matricular_estudiante(self.est2)
        with self.assertRaises(CupoAgotadoError):
            self.grupo.matricular_estudiante(self.est3)
        self.assertEqual(len(self.grupo.estudiantes), 2)

    def test_retiro_valido(self):
        self.grupo.matricular_estudiante(self.est1)
        self.grupo.retirar_estudiante("E001")
        self.assertEqual(len(self.grupo.estudiantes), 0)
        self.assertIn("sin estudiantes", self.grupo.mostrar_estudiantes())

    def test_retiro_inexistente(self):
        with self.assertRaises(EstudianteNoMatriculadoError):
            self.grupo.retirar_estudiante("E999")

    def test_busqueda_asignatura_inexistente(self):
        self.assertIs(self.sistema.buscar_asignatura("POO"), self.asignatura)
        with self.assertRaises(AsignaturaNoEncontradaError):
            self.sistema.buscar_asignatura("NO-EXISTE")

    def test_busqueda_programa_inexistente(self):
        self.assertIs(self.sistema.buscar_programa("IS"), self.programa)
        with self.assertRaises(ProgramaNoEncontradoError):
            self.sistema.buscar_programa("NO-EXISTE")

    def test_horarios_invalidos(self):
        with self.assertRaises(ValueError):
            Horario("Lunes", "12:00", "09:00", "A")
        with self.assertRaises(ValueError):
            Horario("Lunes", "25:00", "26:00", "A")

    def test_matricular_objeto_incorrecto_no_cambia_cupo(self):
        with self.assertRaises(ValueError):
            self.grupo.matricular_estudiante("E001")
        self.assertEqual(len(self.grupo.estudiantes), 0)

    def test_lista_inmutable_desde_fuera(self):
        self.assertIsInstance(self.grupo.estudiantes, tuple)
        with self.assertRaises(AttributeError):
            self.grupo.estudiantes.append(self.est1)

    def test_continuidad_tras_excepcion(self):
        with self.assertRaises(EstudianteNoMatriculadoError):
            self.grupo.retirar_estudiante("NO-EXISTE")
        self.grupo.matricular_estudiante(self.est1)
        self.assertEqual(len(self.grupo.estudiantes), 1)


if __name__ == "__main__":
    unittest.main()
