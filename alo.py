class Alumno:
    # Constructor con atributos vacíos
    def __init__(self):
        self.__nombre = None
        self.__apellido_paterno = None
        self.__apellido_materno = None
        self.__no_control = None
        self.__semestre = None

    # Métodos para establecer los valores (setters)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos para obtener los valores (getters)
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre

    def get_completo(self):
        return f"{self.get_nombre() or 'No definido'} {self.get_apellido_paterno() or 'No definido'} {self.get_apellido_materno() or 'No definido'}"

    # Método para mostrar la información del alumno
    def mostrar_info(self):
        return (f"Nombre: {self.get_nombre() or 'No definido'} "
                f"{self.get_apellido_paterno() or 'No definido'} "
                f"{self.get_apellido_materno() or 'No definido'}, "
                f"No. Control: {self.get_no_control() or 'No definido'}, "
                f"Semestre: {self.get_semestre() or 'No definido'}")
