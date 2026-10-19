# Sistema de Gestión Académica — Actividad colaborativa N.º 1

**Universidad de Manizales — Programación Orientada a Objetos (Python)**

## Integrantes

- Juan David Gálvez Molina.


## Descripción general

Primera versión de un sistema académico que organiza los datos de programas académicos, asignaturas y personas vinculadas a una universidad: estudiantes, docentes y administrativos. Incluye consultas de información, cambios validados y un reporte polimórfico conjunto. Es un programa de demostración ejecutable desde la terminal; no implementa base de datos ni interfaz gráfica porque no son exigencias de esta actividad.

## Estructura de archivos

- `main.py`: programa principal. Crea objetos, ejecuta actualizaciones válidas e inválidas y genera el reporte polimórfico.
- `modelos.py`: clases `Persona`, `ProgramaAcademico`, `Asignatura`, `Estudiante`, `Docente` y `Administrativo`.
- `test_sistema.py`: pruebas automatizadas con `unittest`.
- `.gitignore`: excluye archivos temporales y entornos locales.
- `README.md`: documentación e instrucciones.

## Requisitos y ejecución

Requiere **Python 3.10 o superior**. No necesita instalar bibliotecas adicionales.

```powershell
cd "$HOME\SistemaGestionAcademica"
python main.py
```

Para ejecutar las pruebas:

```powershell
python -m unittest -v
```

## Aplicación de POO por fases

1. **Clases, objetos y constructores:** `Persona`, `ProgramaAcademico` y `Asignatura` inicializan sus atributos con `__init__`; `main.py` crea sus instancias.
2. **Encapsulamiento y validación:** se utilizan atributos privados (`__atributo`) y propiedades `@property` y setters. Por ejemplo, se rechazan correos vacíos, semestres no positivos y créditos no positivos, sin alterar el valor anterior.
3. **Herencia:** `Estudiante`, `Docente` y `Administrativo` heredan de `Persona` y reutilizan su constructor mediante `super()`.
4. **Sobreescritura:** las tres clases especializadas redefinen `mostrar_informacion()` y `realizar_actividad_principal()` para presentar información y conductas propias.
5. **Polimorfismo:** una sola lista reúne dos objetos de cada tipo de persona, y un solo `for` invoca los mismos métodos sobre todos sin condicionales para determinar su clase.

## Pruebas y resultados esperados

Al ejecutar `main.py` se observan dos programas, dos asignaturas, seis personas, tres modificaciones válidas, tres modificaciones inválidas rechazadas y un reporte que demuestra el polimorfismo. Ejecutar `python -m unittest -v` para comprobar las validaciones, consultas, herencia y métodos sobreescritos.

## Uso de inteligencia artificial

Para esta actividad se utilizó ChatGPT (OpenAI) como herramienta de apoyo para plantear la organización del proyecto, generar una propuesta inicial de código, documentar las clases y preparar pruebas. La autoría académica, revisión, comprensión, ejecución y validación del código presentado corresponden a al estudiante JUAN DAVID GALVEZ, quien reviso y comprendio todas las implementaciones.

## Entrega y control de versiones

El repositorio se entrega mediante enlace de GitHub. correspondiente a la Actividad 1 y no se modificara esa versión después de la fecha de cierre. Los desarrollos posteriores quedaran identificados por versiones o commits nuevos.
