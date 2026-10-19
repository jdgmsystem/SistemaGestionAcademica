"""Modelos del Sistema de Gestión Académica.

Actividad colaborativa N.º 1 - Programación Orientada a Objetos.
Se aplican clases, constructores, encapsulamiento, herencia,
sobreescritura de métodos y polimorfismo.
"""


def _texto_obligatorio(valor, campo):
    """Valida texto no vacío y devuelve su representación sin espacios extremos."""
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{campo} no puede estar vacío.")
    return valor.strip()


def _entero_positivo(valor, campo):
    if isinstance(valor, bool) or not isinstance(valor, int) or valor <= 0:
        raise ValueError(f"{campo} debe ser un número entero mayor que cero.")
    return valor


class Persona:
    """Clase base para las personas vinculadas a la universidad."""

    def __init__(self, identificacion, nombre, correo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, valor):
        self.__identificacion = _texto_obligatorio(valor, "La identificación")

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = _texto_obligatorio(valor, "El nombre")

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        self.__correo = _texto_obligatorio(valor, "El correo electrónico")

    def mostrar_informacion(self):
        return (f"Identificación: {self.identificacion}\n"
                f"Nombre: {self.nombre}\n"
                f"Correo: {self.correo}")

    def realizar_actividad_principal(self):
        raise NotImplementedError("Cada tipo de persona define su actividad.")


class ProgramaAcademico:
    """Representa un programa ofrecido por una facultad."""

    def __init__(self, codigo, nombre, facultad, semestres):
        self.codigo = codigo
        self.nombre = nombre
        self.facultad = facultad
        self.semestres = semestres

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        self.__codigo = _texto_obligatorio(valor, "El código del programa")

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = _texto_obligatorio(valor, "El nombre del programa")

    @property
    def facultad(self):
        return self.__facultad

    @facultad.setter
    def facultad(self, valor):
        self.__facultad = _texto_obligatorio(valor, "La facultad")

    @property
    def semestres(self):
        return self.__semestres

    @semestres.setter
    def semestres(self, valor):
        self.__semestres = _entero_positivo(valor, "El número de semestres")

    def mostrar_informacion(self):
        return (f"Programa: {self.nombre} (código {self.codigo})\n"
                f"Facultad: {self.facultad}\n"
                f"Semestres: {self.semestres}")


class Asignatura:
    """Representa una asignatura y su vinculación a un programa."""

    def __init__(self, codigo, nombre, creditos, programa):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.programa = programa

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        self.__codigo = _texto_obligatorio(valor, "El código de la asignatura")

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = _texto_obligatorio(valor, "El nombre de la asignatura")

    @property
    def creditos(self):
        return self.__creditos

    @creditos.setter
    def creditos(self, valor):
        self.__creditos = _entero_positivo(valor, "El número de créditos")

    @property
    def programa(self):
        return self.__programa

    @programa.setter
    def programa(self, valor):
        if not isinstance(valor, ProgramaAcademico):
            raise ValueError("La asignatura requiere un ProgramaAcademico válido.")
        self.__programa = valor

    def mostrar_informacion(self):
        return (f"Asignatura: {self.nombre} (código {self.codigo})\n"
                f"Créditos: {self.creditos}\n"
                f"Programa: {self.programa.nombre}")


class Estudiante(Persona):
    """Especialización de Persona para estudiantes."""

    def __init__(self, identificacion, nombre, correo,
                 codigo_estudiantil, programa, semestre, promedio):
        super().__init__(identificacion, nombre, correo)
        self.__codigo_estudiantil = _texto_obligatorio(
            codigo_estudiantil, "El código estudiantil")
        if not isinstance(programa, ProgramaAcademico):
            raise ValueError("El estudiante requiere un ProgramaAcademico válido.")
        self.__programa = programa
        self.__semestre = _entero_positivo(semestre, "El semestre")
        if isinstance(promedio, bool) or not isinstance(promedio, (int, float)) or not 0 <= promedio <= 5:
            raise ValueError("El promedio debe estar entre 0 y 5.")
        self.__promedio = float(promedio)

    def mostrar_informacion(self):
        return ("[ESTUDIANTE]\n" + super().mostrar_informacion()
                + f"\nCódigo estudiantil: {self.__codigo_estudiantil}"
                + f"\nPrograma: {self.__programa.nombre}"
                + f"\nSemestre: {self.__semestre}"
                + f"\nPromedio acumulado: {self.__promedio:.2f}")

    def realizar_actividad_principal(self):
        return (f"{self.nombre} estudia {self.__programa.nombre} "
                f"y cursa el semestre {self.__semestre}.")


class Docente(Persona):
    """Especialización de Persona para docentes."""

    def __init__(self, identificacion, nombre, correo,
                 numero_empleado, facultad, tipo_contratacion, horas_semanales):
        super().__init__(identificacion, nombre, correo)
        self.__numero_empleado = _texto_obligatorio(numero_empleado, "El número de empleado")
        self.__facultad = _texto_obligatorio(facultad, "La facultad")
        self.__tipo_contratacion = _texto_obligatorio(tipo_contratacion, "El tipo de contratación")
        self.__horas_semanales = _entero_positivo(horas_semanales, "Las horas semanales")

    def mostrar_informacion(self):
        return ("[DOCENTE]\n" + super().mostrar_informacion()
                + f"\nNúmero de empleado: {self.__numero_empleado}"
                + f"\nFacultad: {self.__facultad}"
                + f"\nTipo de contratación: {self.__tipo_contratacion}"
                + f"\nHoras semanales: {self.__horas_semanales}")

    def realizar_actividad_principal(self):
        return f"{self.nombre} orienta clases en la facultad {self.__facultad}."


class Administrativo(Persona):
    """Especialización de Persona para personal administrativo."""

    def __init__(self, identificacion, nombre, correo,
                 numero_empleado, dependencia, cargo, jornada):
        super().__init__(identificacion, nombre, correo)
        self.__numero_empleado = _texto_obligatorio(numero_empleado, "El número de empleado")
        self.__dependencia = _texto_obligatorio(dependencia, "La dependencia")
        self.__cargo = _texto_obligatorio(cargo, "El cargo")
        self.__jornada = _texto_obligatorio(jornada, "La jornada")

    def mostrar_informacion(self):
        return ("[ADMINISTRATIVO]\n" + super().mostrar_informacion()
                + f"\nNúmero de empleado: {self.__numero_empleado}"
                + f"\nDependencia: {self.__dependencia}"
                + f"\nCargo: {self.__cargo}"
                + f"\nJornada: {self.__jornada}")

    def realizar_actividad_principal(self):
        return (f"{self.nombre} trabaja como {self.__cargo} "
                f"en {self.__dependencia}.")
