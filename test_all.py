#!/usr/bin/python3
import unittest
import time
from io import StringIO
from unittest.mock import patch
import os

from base import Base
from rectangle import Rectangle
from square import Square


class TestBase(unittest.TestCase):
    def test_json_serialization(self):
        # (Prueba de funcionalidad) Validamos que Base convierta listas de diccionarios a JSON
        # y que pueda deserializar de vuelta sin pérdida de información.
        d = [{'id': 1, 'size': 5}]
        json_str = Base.to_json_string(d)
        self.assertEqual(json_str, '[{"id": 1, "size": 5}]')
        self.assertEqual(Base.from_json_string(json_str), d)

    def test_file_integration(self):
        # (Prueba de integración) Probamos la integración de Base con Square.
        # Guardamos un objeto en archivo y lo cargamos de nuevo para comprobar persistencia.
        s1 = Square(3, 1, 2, id=99)
        Square.save_to_file([s1])
        loaded = Square.load_from_file()
        self.assertEqual(str(loaded[0]), str(s1))


class TestRectangle(unittest.TestCase):
    def test_functional_area(self):
        # (Prueba de funcionalidad) Validamos que el cálculo del área sea correcto.
        r = Rectangle(4, 5)
        print(f"\nÁrea calculada: {r.area()}")
        self.assertEqual(r.area(), 20)

    def test_usability_str(self):
        # (Prueba de usabilidad) Comprobamos que la salida de __str__ sea clara y legible.
        r = Rectangle(3, 2, 1, 1, id=77)
        print(f"\nRepresentación en cadena: {r}")
        self.assertEqual(str(r), "[Rectangle] (77) 1/1 - 3/2")

    def test_performance_large_area(self):
        # (Prueba de rendimiento) Evaluamos tiempos de ejecución con valores grandes.
        r = Rectangle(10000, 20000)
        start = time.time()
        result = r.area()
        end = time.time()
        print(f"\nÁrea de un rectángulo grande: {result}, tiempo de ejecución: {end - start} ms")
        self.assertEqual(result, 10000 * 20000)
        self.assertLess(end - start, 0.05)

    def test_security_invalid_inputs(self):
        # (Prueba de seguridad) Validamos que se rechacen entradas inválidas.
        with self.assertRaises(TypeError):
            Rectangle("a", 5)
        with self.assertRaises(ValueError):
            Rectangle(-1, 5)

    def test_integration_with_base(self):
        # (Prueba de integración) Confirmamos que Rectangle hereda de Base
        # y que to_dictionary devuelve la estructura esperada.
        r = Rectangle(2, 3)
        self.assertTrue(isinstance(r, Base))
        d = r.to_dictionary()
        print(f"\nDiccionario del rectángulo: {d}")
        self.assertEqual(d, {'id': r.id, 'width': 2, 'height': 3, 'x': 0, 'y': 0})

    def test_acceptance_flow(self):
        # (Prueba de aceptación) Flujo completo: crear, guardar, cargar y verificar consistencia.
        r = Rectangle(4, 6, 2, 1, id="case2")
        Rectangle.save_to_file([r])
        loaded = Rectangle.load_from_file()
        self.assertEqual(str(loaded[0]), "[Rectangle] (case2) 2/1 - 4/6")


class TestSquare(unittest.TestCase):
    def test_functional_area(self):
        # (Prueba de funcionalidad) Validamos que el área de un cuadrado se calcule correctamente.
        r = Square(5)
        self.assertEqual(r.area(), 25)

    def test_usability_str(self):
        # (Prueba de usabilidad) Comprobamos que la representación en texto sea clara.
        r = Square(3, 1, 2, id="case1")
        self.assertEqual(str(r), "[Square] (case1) 1/2 - 3")

    def test_performance_area(self):
        # (Prueba de rendimiento) Evaluamos tiempos de ejecución con un cuadrado grande.
        r = Square(10000)
        start = time.time()
        result = r.area()
        end = time.time()
        self.assertEqual(result, 10000**2)
        self.assertLess(end - start, 0.05)

    def test_security_invalid_inputs(self):
        # (Prueba de seguridad) Validamos que Square rechace entradas inválidas.
        with self.assertRaises(TypeError):
            Square("<script>")
        with self.assertRaises(ValueError):
            Square(-999)

    def test_integration_with_rectangle(self):
        # (Prueba de integración) Confirmamos que Square hereda de Rectangle y Base.
        s = Square(4)
        self.assertTrue(isinstance(s, Rectangle))
        self.assertTrue(isinstance(s, Base))
        d = s.to_dictionary()
        self.assertEqual(d, {'id': s.id, 'size': 4, 'x': 0, 'y': 0})

    def test_acceptance_flow(self):
        # (Prueba de aceptación) Flujo completo: crear, guardar, cargar y verificar consistencia.
        s = Square(4, 2, 1, id="user_case")
        Square.save_to_file([s])
        loaded = Square.load_from_file()
        self.assertEqual(str(loaded[0]), "[Square] (user_case) 2/1 - 4")


if __name__ == "__main__":
    unittest.main(verbosity=2)