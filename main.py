"""Demostración integrada de las actividades 1 y 2 del Sistema Académico.

Ejecutar con: python main.py
"""

from modelos import Administrativo, Asignatura, Docente, Estudiante, Persona, ProgramaAcademico
from grupo_academico import GrupoAcademico
from sistema_academico import SistemaAcademico
from excepciones import (
    EstudianteYaMatriculadoError,
    CupoAgotadoError,
    EstudianteNoMatriculadoError,
    AsignaturaNoEncontradaError,
    ProgramaNoEncontradoError,
)


def intentar_cambio(descripcion, accion):
    """Informa si una actualización se realizó o fue rechazada por validación."""
    try:
        accion()
        print(f"CORRECTO: {descripcion}")
    except ValueError as error:
        print(f"RECHAZADO: {descripcion} -> {error}")


def ejecutar_operacion(descripcion, accion):
    """Captura excepciones de negocio e impide que detengan el programa."""
    try:
        print(f"CORRECTO: {accion()}")
    except (EstudianteYaMatriculadoError, CupoAgotadoError,
            EstudianteNoMatriculadoError, AsignaturaNoEncontradaError,
            ProgramaNoEncontradoError) as error:
        print(f"EXCEPCIÓN CONTROLADA ({descripcion}): {error}")


def main():
    print("=" * 62)
    print("SISTEMA DE GESTIÓN ACADÉMICA - ACTIVIDAD COLABORATIVA 1")
    print("=" * 62)

    # Fase 1: programas y asignaturas creados con constructores.
    sistemas = ProgramaAcademico("IS01", "Ingeniería de Sistemas", "Ciencias e Ingenierías", 10)
    contaduria = ProgramaAcademico("CP01", "Contaduría Pública", "Ciencias Contables", 9)
    poo = Asignatura("PRG201", "Programación Orientada a Objetos", 3, sistemas)
    auditoria = Asignatura("AUD301", "Auditoría", 4, contaduria)

    print("\nFASE 1: PROGRAMAS ACADÉMICOS")
    for programa in (sistemas, contaduria):
        print(programa.mostrar_informacion(), "\n")

    print("FASE 1: ASIGNATURAS")
    for asignatura in (poo, auditoria):
        print(asignatura.mostrar_informacion(), "\n")

    # Fases 3 y 4: herencia, super() y métodos sobreescritos.
    # Fase 5: todos los tipos se almacenan en una única colección.
    personas = [
        Estudiante("1001", "Ana Torres", "ana@universidad.edu", "E001", sistemas, 3, 4.3),
        Estudiante("1002", "Luis Pérez", "luis@universidad.edu", "E002", contaduria, 5, 4.0),
        Docente("2001", "Marta Gómez", "marta@universidad.edu", "D001",
                "Ciencias e Ingenierías", "Tiempo completo", 40),
        Docente("2002", "Pedro Díaz", "pedro@universidad.edu", "D002",
                "Ciencias Contables", "Medio tiempo", 20),
        Administrativo("3001", "Elena Rojas", "elena@universidad.edu", "A001",
                       "Registro Académico", "Auxiliar", "Diurna"),
        Administrativo("3002", "Carlos Mora", "carlos@universidad.edu", "A002",
                       "Bienestar Universitario", "Coordinador", "Mixta"),
    ]

    # Fase 2: modificaciones controladas usando propiedades y validaciones.
    print("FASE 2: MODIFICACIONES VÁLIDAS")
    personas[0].correo = "ana.torres@universidad.edu"
    sistemas.semestres = 9
    poo.creditos = 4
    print(f"Correo actualizado: {personas[0].correo}")
    print(f"Semestres actualizados: {sistemas.semestres}")
    print(f"Créditos actualizados: {poo.creditos}")

    print("\nFASE 2: TRES MODIFICACIONES INVÁLIDAS")
    intentar_cambio("Correo vacío", lambda: setattr(personas[0], "correo", ""))
    intentar_cambio("Cero semestres", lambda: setattr(sistemas, "semestres", 0))
    intentar_cambio("Créditos negativos", lambda: setattr(poo, "creditos", -2))
    print("Valores conservados después de los rechazos:")
    print(f"  Correo: {personas[0].correo}")
    print(f"  Semestres: {sistemas.semestres}")
    print(f"  Créditos: {poo.creditos}")

    print("\nFASES 3, 4 Y 5: REPORTE POLIMÓRFICO DE PERSONAS")
    # No se pregunta por tipos: cada objeto ejecuta su propia versión.
    for persona in personas:
        print("-" * 62)
        print(persona.mostrar_informacion())
        print("Actividad principal:", persona.realizar_actividad_principal())

    # AC2 fase 1: Persona es abstracta, sus especializaciones se mantienen.
    print("\nAC2 - FASE 1: PERSONA ABSTRACTA")
    try:
        Persona("999", "Sin rol", "correo@universidad.edu")
    except TypeError as error:
        print("CONTROLADO: No se puede crear Persona directamente:", error)

    # AC2 fases 2 y 3: se aprovechan los objetos construidos en la AC1.
    print("\nAC2 - FASES 2 Y 3: GRUPOS, OBJETOS Y COMPOSICIÓN")
    sistema = SistemaAcademico()
    for programa in (sistemas, contaduria):
        sistema.registrar_programa(programa)
    for asignatura in (poo, auditoria):
        sistema.registrar_asignatura(asignatura)

    grupo_poo = GrupoAcademico("POO-A", poo, personas[2], 2,
                               "Lunes", "08:00", "10:00", "A-201")
    grupo_auditoria = GrupoAcademico("AUD-B", auditoria, personas[3], 1,
                                    "Miércoles", "14:00", "16:00", "B-103")
    sistema.registrar_grupo(grupo_poo)
    sistema.registrar_grupo(grupo_auditoria)
    for grupo in (grupo_poo, grupo_auditoria):
        print("-" * 62)
        print(grupo.mostrar_informacion_grupo())

    # AC2 fase 4: matrículas y excepciones lanzadas en el dominio.
    print("\nAC2 - FASE 4: MATRÍCULAS, RETIROS Y EXCEPCIONES")
    estudiante_adicional = Estudiante(
        "1003", "Sofía Ramírez", "sofia@universidad.edu",
        "E003", sistemas, 2, 4.5)
    aspirante_sin_cupo = Estudiante(
        "1004", "Daniel Ruiz", "daniel@universidad.edu",
        "E004", sistemas, 4, 4.1)
    ejecutar_operacion("Matrícula válida 1", lambda: grupo_poo.matricular_estudiante(personas[0]))
    ejecutar_operacion("Matrícula válida 2", lambda: grupo_poo.matricular_estudiante(estudiante_adicional))
    ejecutar_operacion("Duplicado", lambda: grupo_poo.matricular_estudiante(personas[0]))
    ejecutar_operacion("Capacidad", lambda: grupo_poo.matricular_estudiante(aspirante_sin_cupo))
    ejecutar_operacion("Matrícula segundo grupo", lambda: grupo_auditoria.matricular_estudiante(personas[1]))
    print("\nEstudiantes antes del retiro:")
    print(grupo_poo.mostrar_estudiantes())
    ejecutar_operacion("Retiro válido", lambda: grupo_poo.retirar_estudiante("E003"))
    ejecutar_operacion("Retiro inexistente", lambda: grupo_poo.retirar_estudiante("E003"))
    ejecutar_operacion("Asignatura inexistente", lambda: sistema.buscar_asignatura("NO-EXISTE").nombre)
    ejecutar_operacion("Programa inexistente", lambda: sistema.buscar_programa("NO-EXISTE").nombre)
    print("\nEstudiantes matriculados al finalizar:")
    print(grupo_poo.mostrar_estudiantes())
    print("\nCONTINUIDAD CONFIRMADA: El sistema sigue funcionando después de las excepciones.")
    print("Demostración de las actividades 1 y 2 terminada correctamente.")


if __name__ == "__main__":
    main()
