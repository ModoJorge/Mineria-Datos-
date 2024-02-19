"""Negative unit tests for hotel_management module."""
# test_hotel_management_negative.py

import unittest
import os
import json
from hotel_management import Hotel, Room, load_hotel, save_hotel


class TestHotelManagementNegative(unittest.TestCase):
    """Docstring for the class."""
    def setUp(self):
        """Docstring for the method."""
        # Setup is run before each test method.
        # It initializes a hotel with rooms.
        self.hotel = Hotel("Test Hotel", "123 Test Street")
        self.hotel.add_room(Room(101, 100))
        # Add a room with number 101 and price 100
        self.hotel.add_room(Room(102, 150))
        # Add another room with number 102 and price 150

    def test_reserve_nonexistent_room(self):
        """Docstring for the method."""
        # Test attempting to reserve a room that does not exist.
        # It should raise a ValueError since the
        # Sroom number 999 is not added in setup.
        with self.assertRaises(ValueError):
            self.hotel.reserve_room(999)

    def test_reserve_occupied_room(self):
        """Docstring for the method."""
        # Test attempting to reserve a room that is already occupied.
        # First, we reserve a room to occupy it.
        # SThen we attempt to reserve it again, which should r
        self.hotel.reserve_room(101)
        with self.assertRaises(ValueError):
            self.hotel.reserve_room(101)

    def test_cancel_nonexistent_reservation(self):
        """Docstring for the method."""
        # Test attempting to cancel a reservation that does not exist.
        # Since room number 999 is not reserved or even added,
        # it should raise a ValueError.
        with self.assertRaises(ValueError):
            self.hotel.cancel_reservation(999)

    def test_load_corrupt_file(self):
        """Docstring for the method."""
        # Test loading a corrupt JSON file.
        # It should raise a JSONDecodeError since the JSON format is incorrect.
        with open('corrupt_file.json', 'w', encoding='utf-8') as f:
            f.write('{"this is": "corrupt json file}')
            # Intentionally corrupt JSON content.
        with self.assertRaises(json.JSONDecodeError):
            load_hotel('corrupt_file.json')
    os.remove('corrupt_file.json')  # Clean up the file after the test.

    def test_save_to_protected_file(self):
        """Docstring for the method."""
        # Test saving to a protected file, which should raise a PermissionError
        # due to write permissions.
        filename = 'protected_file.json'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('{}')  # Create the file to protect.
        os.chmod(filename, 0o444)  # Make the file read-only.
        # The save_hotel function should raise a PermissionError when trying
        # to write to a read-only file.
        with self.assertRaises(PermissionError):
            save_hotel(self.hotel, filename)

        os.chmod(filename, 0o666)  # Restore write permissions.
        os.remove(filename)  # Clean up the file after the test.


# This allows the tests to be run from the command line.
if __name__ == '__main__':
    unittest.main()
