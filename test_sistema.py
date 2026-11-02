"""Pruebas automáticas básicas sin dependencias externas.

Ejecutar con: python -m unittest -v
"""

import unittest

from modelos import Administrativo, Asignatura, Docente, Estudiante, Persona, ProgramaAcademico


class PruebasSistemaAcademico(unittest.TestCase):
    def setUp(self):
        self.programa = ProgramaAcademico("IS", "Ingeniería de Sistemas", "Ingenierías", 10)
        self.asignatura = Asignatura("POO", "Programación POO", 3, self.programa)
        self.persona = Estudiante("123", "Laura", "laura@correo.edu", "E123", self.programa, 2, 4.0)

    def test_constructores_y_consultas(self):
        self.assertIn("Ingeniería de Sistemas", self.programa.mostrar_informacion())
        self.assertIn("Programación POO", self.asignatura.mostrar_informacion())
        self.assertIn("Laura", self.persona.mostrar_informacion())

    def test_cambios_validos(self):
        self.persona.correo = "nuevo@correo.edu"
        self.programa.semestres = 8
        self.asignatura.creditos = 5
        self.assertEqual(self.persona.correo, "nuevo@correo.edu")
        self.assertEqual(self.programa.semestres, 8)
        self.assertEqual(self.asignatura.creditos, 5)

    def test_cambios_invalidos_no_alteran_valores(self):
        with self.assertRaises(ValueError):
            self.persona.correo = ""
        with self.assertRaises(ValueError):
            self.programa.semestres = 0
        with self.assertRaises(ValueError):
            self.asignatura.creditos = -1
        self.assertEqual(self.persona.correo, "laura@correo.edu")
        self.assertEqual(self.programa.semestres, 10)
        self.assertEqual(self.asignatura.creditos, 3)

    def test_herencia_y_metodos_sobreescritos(self):
        estudiante = Estudiante("1", "Est 1", "e@u.edu", "E1", self.programa, 2, 4.2)
        docente = Docente("2", "Doc 1", "d@u.edu", "D1", "Ingenierías", "Planta", 40)
        administrativo = Administrativo("3", "Adm 1", "a@u.edu", "A1", "Rectoría", "Analista", "Diurna")
        for persona in (estudiante, docente, administrativo):
            self.assertIsInstance(persona, Persona)
            self.assertIn("Identificación", persona.mostrar_informacion())
            self.assertIsInstance(persona.realizar_actividad_principal(), str)
        self.assertIn("semestre", estudiante.realizar_actividad_principal())
        self.assertIn("orienta clases", docente.realizar_actividad_principal())
        self.assertIn("Analista", administrativo.realizar_actividad_principal())

    def test_tipos_invalidos(self):
        with self.assertRaises(ValueError):
            Asignatura("A", "Materia", 2, "No es un programa")
        with self.assertRaises(ValueError):
            ProgramaAcademico("X", "Nombre", "Facultad", -2)


if __name__ == "__main__":
    unittest.main()
