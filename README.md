# Sistema de Gestión Académica — Actividades 1 y 2

**Universidad de Manizales | Programación Orientada a Objetos (Python)**

## Integrante

- Juan David Gálvez Molina.

**Modalidad:** desarrollo individual autorizado por el docente.

## Descripción general

Este repositorio contiene el mismo Sistema de Gestión Académica desarrollado durante la Actividad Colaborativa N.º 1 y ampliado en la Actividad Colaborativa N.º 2. La primera versión representa programas, asignaturas, estudiantes, docentes y administrativos mediante programación orientada a objetos. La segunda incorpora una clase abstracta, grupos académicos con horario propio, operaciones de matrícula y retiro, búsquedas y excepciones personalizadas.

La solución es un programa de consola escrito en Python. No utiliza dependencias externas, base de datos ni interfaz gráfica porque no forman parte de los requisitos de esta etapa.

## Organización del proyecto

| Archivo | Función |
| --- | --- |
| `main.py` | Ejecuta demostraciones de las dos actividades y captura excepciones. |
| `modelos.py` | Define `Persona`, `Estudiante`, `Docente`, `Administrativo`, `ProgramaAcademico` y `Asignatura`, con encapsulamiento, validaciones y polimorfismo. |
| `grupo_academico.py` | Define `GrupoAcademico` y `Horario`; gestiona la matrícula, el retiro y la consulta de estudiantes. |
| `sistema_academico.py` | Mantiene los catálogos de programas, asignaturas y grupos; implementa las búsquedas. |
| `excepciones.py` | Define las excepciones personalizadas del dominio académico. |
| `test_sistema.py` | Cinco pruebas de compatibilidad con la primera actividad. |
| `test_actividad2.py` | Dieciséis pruebas de la ampliación. |
| `Documento Decisiones Diseno AC2.pdf` | Documento final de Decisiones de Diseño de la Actividad N.º 2. |
| `.gitignore` | Excluye los archivos temporales de Python y los entornos locales. |
| `README.md` | Documentación e instrucciones de ejecución. |

## Requisitos y ejecución

Se necesita **Python 3.10 o superior**; la ejecución de verificación se realizó con Python 3.14.7. No se requieren bibliotecas adicionales.

Dentro de la carpeta raíz del proyecto, ejecutar:

```powershell
python main.py
```

Para comprobar todas las pruebas automáticas:

```powershell
python -m unittest discover -v
```

Resultado verificado: **21 pruebas satisfactorias** (cinco correspondientes a la primera versión y dieciséis de la ampliación).

## Actividad N.º 1: fundamentos que se conservan

El sistema mantiene clases, objetos y constructores, así como propiedades y métodos con validaciones para proteger atributos. `Estudiante`, `Docente` y `Administrativo` heredan de `Persona`, sobrescriben `mostrar_informacion()` y definen su comportamiento de `realizar_actividad_principal()`. El archivo principal conserva un recorrido de una colección heterogénea para demostrar polimorfismo sin condicionales por tipo de persona.

## Actividad N.º 2: evolución del sistema

**Clases abstractas.** `Persona` utiliza `ABC` y declara `realizar_actividad_principal()` mediante `@abstractmethod`. Por eso no puede instanciarse directamente. Las tres clases derivadas continúan implementando dicho método.

**Grupos académicos.** `GrupoAcademico` recibe objetos preexistentes de `Asignatura` y `Docente`, conserva una colección privada de estudiantes, valida la capacidad del grupo y proporciona `mostrar_informacion_grupo()`, `matricular_estudiante()`, `retirar_estudiante()` y `mostrar_estudiantes()`.

**Composición.** Cada grupo construye internamente su propio objeto `Horario` a partir del día, la hora de inicio, la hora de finalización y el salón. Esta relación es de composición, no de herencia: un grupo **tiene un** horario, pero no **es un** horario. Una misma asignatura puede ofrecerse en grupos distintos.

**Excepciones personalizadas.** Las clases `EstudianteYaMatriculadoError`, `CupoAgotadoError`, `EstudianteNoMatriculadoError`, `AsignaturaNoEncontradaError` y `ProgramaNoEncontradoError` se definen en `excepciones.py`. Se lanzan en los métodos que detectan cada situación y se capturan en `main.py` mediante `try/except`, con mensajes legibles y sin detener el resto de la demostración.

## Pruebas mínimas de funcionamiento

El archivo `main.py` demuestra: el impedimento de crear `Persona` directamente; la creación de programas, asignaturas, estudiantes, docentes y horarios; al menos dos grupos; matrículas correctas; rechazo de duplicados y cupos completos; retiro exitoso e intento de retirar un código inexistente; búsquedas fallidas de asignaturas y programas; y continuidad de la ejecución después de controlar los errores.

## Documento de Decisiones de Diseño

El documento técnico se entrega como **`Documento Decisiones Diseno AC2.pdf`**, con portada, introducción, descripción de la implementación, análisis de abstracción, composición, excepciones, polimorfismo, resultados de pruebas, conclusiones y declaración de inteligencia artificial.

## Uso de herramientas de inteligencia artificial

Se utilizó ChatGPT (OpenAI) como apoyo para analizar los requerimientos, proponer e implementar la evolución del código, documentar decisiones de diseño y preparar pruebas automáticas. El estudiante conserva la responsabilidad académica de revisar, comprender, ejecutar, comprobar y explicar el contenido entregado. Esta declaración también figura en el Documento de Decisiones de Diseño.

## Versiones y entrega

El repositorio es el mismo de la Actividad N.º 1: `https://github.com/jdgmsystem/SistemaGestionAcademica`.

La primera entrega permanece identificada con la etiqueta `actividad-1`. Para la segunda actividad debe crearse y publicarse la etiqueta **`Entrega_AC2`**, sin desplazar ni modificar la etiqueta anterior. El enlace de entrega corresponde al mismo repositorio, indicando la versión de la Actividad N.º 2.
