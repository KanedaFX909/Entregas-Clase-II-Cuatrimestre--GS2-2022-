#!/usr/bin/python3
from empleado import Empleado
class EmpleadoPermanente(Empleado):
    def __init__(self, nombre, apellido, dni, salario, antiguedad):
        self.antiguedad = antiguedad
        super().__init__(nombre, apellido, dni, salario)

    def calcular_comision(self):
        comision = self.salario * self.antiguedad / 100
        return comision

    #def mostrar_datos(self):
    #    texto += f"Antigüedad: {self.antiguedad}\n"
    #    return texto & super().mostrar_datos(self.texto)
    # el dato antiguedad, es propio de PERMANENTE
    # Si cambio el nombre de la variable texto por uno propio de la clase se rompe
    # Si dejo la variable texro como esta, error=unbound local variable referred before
    # occurs when we reference a local variable before assigning a value to it in a function