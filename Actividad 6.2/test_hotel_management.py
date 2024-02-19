"""Unit tests for hotel_management module."""
import unittest
from hotel_management import Hotel, Room, Customer, save_hotel, load_hotel


class TestCustomer(unittest.TestCase):
    """Docstring for the class."""
    def test_customer_creation(self):
        """Docstring for the method."""
        customer = Customer("John Doe", "john.doe@example.com")
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.email, "john.doe@example.com")


class TestHotelManagement(unittest.TestCase):
    """Docstring for the class."""
    def test_hotel_creation(self):
        """Docstring for the method."""
        hotel = Hotel("Test Hotel", "123 Test Address")
        self.assertEqual(hotel.name, "Test Hotel")
        self.assertEqual(hotel.address, "123 Test Address")

    def test_room_addition(self):
        """Docstring for the method."""
        hotel = Hotel("Test Hotel", "123 Test Address")
        room = Room(101, 100)
        hotel.add_room(room)
        self.assertEqual(len(hotel.rooms), 1)
        self.assertEqual(hotel.rooms[0].number, 101)

    def test_add_room_method(self):
        """Docstring for the method."""
        hotel = Hotel("Test Hotel", "123 Test Address")
        room = Room(101, 100)
        hotel.add_room(room)
        self.assertEqual(len(hotel.rooms), 1)
        self.assertEqual(hotel.rooms[0].number, 101)

    def test_room_constructor(self):
        """Docstring for the method."""
        room = Room(101, 50)  # Assuming Room class has 'number' and 'price'
        self.assertEqual(room.number, 101)
        self.assertEqual(room.price, 50)

    def test_reserve_room(self):
        """Docstring for the method."""
        hotel = Hotel("Test Hotel", "123 Test Address")
        room = Room(101, 100)
        hotel.add_room(room)

        with self.assertRaises(ValueError):
            hotel.reserve_room(102)  # Try to reserve a non-existent room

        hotel.reserve_room(101)  # Reserve an available room
        self.assertTrue(hotel.rooms[0].is_occupied)

        with self.assertRaises(ValueError):
            hotel.reserve_room(101)  # Try to reserve an already occupied room

    def test_cancel_reservation(self):
        """Docstring for the method."""
        hotel = Hotel("Test Hotel", "123 Test Address")
        room = Room(101, 100)
        hotel.add_room(room)

        with self.assertRaises(ValueError):
            hotel.cancel_reservation(102)
            # Try to cancel a reservation for a non-existent room

        with self.assertRaises(ValueError):
            hotel.cancel_reservation(101)
            # Try to cancel a non-existent reservation

        hotel.reserve_room(101)  # Reserve the room first
        self.assertTrue(hotel.rooms[0].is_occupied)

        hotel.cancel_reservation(101)  # Cancel the reservation
        self.assertFalse(hotel.rooms[0].is_occupied)

    def test_save_and_load_hotel(self):
        """Docstring for the method."""
        hotel = Hotel("Test Hotel", "123 Test Address")
        room = Room(101, 100)
        hotel.add_room(room)
        save_hotel(hotel, 'test_hotel.json')

        _ = load_hotel('test_hotel.json')
        self.assertEqual(_.name, hotel.name)
        self.assertEqual(len(_.rooms), 1)
        self.assertEqual(_.rooms[0].number, 101)

    def test_save_hotel_function(self):
        """Docstring for the method."""
        hotel = Hotel("Test Hotel", "123 Test Address")
        room = Room(101, 100)
        hotel.add_room(room)
        save_hotel(hotel, 'test_hotel.json')
        # Add assertions to check the file existence, content, etc.

    def test_load_hotel_function(self):
        """Docstring for the method."""
        hotel = Hotel("Test Hotel", "123 Test Address")
        room = Room(101, 100)
        hotel.add_room(room)
        save_hotel(hotel, 'test_hotel.json')

        _ = load_hotel('test_hotel.json')
        self.assertEqual(_.name, hotel.name)
        self.assertEqual(len(_.rooms), 1)
        self.assertEqual(_.rooms[0].number, 101)

    def test_invalid_file_load_hotel_function(self):
        """Docstring for the method."""
        with self.assertRaises(FileNotFoundError):
            _ = load_hotel('nonexistent_file.json')


if __name__ == '__main__':
    unittest.main()
