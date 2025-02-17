
import unittest
import os  # Importamos os para evitar errores
from hotel import Hotel  # Importamos Hotel desde el archivo hotel.py


class TestHotel(unittest.TestCase):
    """Clase de pruebas unitarias para la clase Hotel."""

    def setUp(self):
        """Setup antes de cada prueba"""
        self.test_file = "test_hotels.json"
        Hotel.save_to_file([], self.test_file)

    def test_create_hotel(self):
        """Prueba la creación de un hotel"""
        Hotel.create_hotel(1, "Test Hotel", "Test City", 10, self.test_file)
        hotels = Hotel.load_from_file(self.test_file)
        self.assertEqual(len(hotels), 1)
        self.assertEqual(hotels[0].name, "Test Hotel")

    def tearDown(self):
        """Eliminar archivos temporales después de las pruebas"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
