"""Module for managing hotel operations such
as room booking and customer management."""

import json


class Hotel:
    """Represents a hotel which can manage rooms and reservations."""

    def __init__(self, name, address):
        """Initialize a new Hotel instance with a name and an address."""
        self.name = name
        self.address = address
        self.rooms = []  # Lista de objetos Room

    def add_room(self, room):
        """Add a room to the hotel's list of rooms."""
        self.rooms.append(room)

    def to_dict(self):
        """Convert the hotel to a dictionary format."""
        return {
            'name': self.name,
            'address': self.address,
            'rooms': [room.to_dict() for room in self.rooms]
        }

    def reserve_room(self, room_number):
        """Reserve a room by its number."""
        room = next(
            (room for room in self.rooms if room.number == room_number),
            None
        )
        if room is None:
            raise ValueError("La habitación no existe.")
        if room.is_occupied:
            raise ValueError("La habitación ya está ocupada.")
        room.is_occupied = True
        return f"Habitación {room_number} reservada con éxito."

    def cancel_reservation(self, room_number):
        """Cancel the reservation of a room by its number."""
        room = next(
            (room for room in self.rooms if room.number == room_number),
            None
        )
        if room is None or not room.is_occupied:
            raise ValueError(
                "No hay una reservación activa para esta habitación."
            )
        room.is_occupied = False
        return (
            f"Reservación de la habitación {room_number}"
            "cancelada con éxito."
        )


class Room:
    # pylint: disable=too-few-public-methods
    """Represents a room in the hotel."""

    def __init__(self, number, price):
        """Initialize a room with a number, price, and occupancy status."""
        self.number = number
        self.price = price
        self.is_occupied = False

    def to_dict(self):
        """Convert the room to a dictionary format."""
        return {
            'number': self.number,
            'price': self.price,
            'is_occupied': self.is_occupied
        }


class Customer:
    # pylint: disable=too-few-public-methods
    """Represents a customer of the hotel."""

    def __init__(self, name, email):
        """Initialize a customer with a name and an email."""
        self.name = name
        self.email = email

    def to_dict(self):
        """Convert the customer to a dictionary format."""
        return {
            'name': self.name,
            'email': self.email
        }


def save_hotel(hotel, filename='hotel_data.json'):
    """Save hotel data to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(hotel.to_dict(), file, indent=4)


def load_hotel(filename='hotel_data.json'):
    """Load hotel data from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    hotel = Hotel(data['name'], data['address'])
    for room_data in data['rooms']:
        room = Room(room_data['number'], room_data['price'])
        room.is_occupied = room_data.get('is_occupied', False)
        hotel.add_room(room)
    return hotel
