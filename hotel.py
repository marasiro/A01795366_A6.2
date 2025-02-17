
import json
import os


class Hotel:
    """Clase para manejar información de hoteles."""

    def __init__(self, hotel_id, name, location, rooms_available):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms_available = rooms_available

    def to_dict(self):
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "rooms_available": self.rooms_available
        }

    @staticmethod
    def create_hotel(hotel_id, name, location, rooms_available, filename="hotels.json"):
        hotels = Hotel.load_from_file(filename)
        hotels.append(Hotel(hotel_id, name, location, rooms_available))
        Hotel.save_to_file(hotels, filename)

    @staticmethod
    def delete_hotel(hotel_id, filename="hotels.json"):
        hotels = [hotel for hotel in Hotel.load_from_file(filename) if hotel.hotel_id != hotel_id]
        Hotel.save_to_file(hotels, filename)

    @staticmethod
    def modify_hotel(hotel_id, name, location, rooms_available, filename="hotels.json"):
        hotels = Hotel.load_from_file(filename)
        for hotel in hotels:
            if hotel.hotel_id == hotel_id:
                hotel.name = name
                hotel.location = location
                hotel.rooms_available = rooms_available
        Hotel.save_to_file(hotels, filename)

    @staticmethod
    def save_to_file(hotels, filename="hotels.json"):
        with open(filename, "w") as file:
            json.dump([hotel.to_dict() for hotel in hotels], file, indent=4)

    @staticmethod
    def load_from_file(filename="hotels.json"):
        if not os.path.exists(filename):
            return []
        try:
            with open(filename, "r") as file:
                return [Hotel(**data) for data in json.load(file)]
        except (json.JSONDecodeError, TypeError):
            return []
