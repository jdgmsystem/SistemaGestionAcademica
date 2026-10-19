"""Demostración de las cinco fases del Sistema de Gestión Académica.

Ejecutar con: python main.py
"""

from modelos import Administrativo, Asignatura, Docente, Estudiante, ProgramaAcademico


def intentar_cambio(descripcion, accion):
    """Informa si una actualización se realizó o fue rechazada por validación."""
    try:
        accion()
        print(f"CORRECTO: {descripcion}")
    except ValueError as error:
        print(f"RECHAZADO: {descripcion} -> {error}")


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

    print("\nDemostración terminada correctamente.")


if __name__ == "__main__":
    main()
