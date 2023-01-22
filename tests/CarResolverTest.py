import unittest
from unittest.mock import MagicMock

from src.CarResolver import CarResolver, BankruptManufacturerException

"""
This is the test class for CarResolver.

The CarResolver class has two dependencies - CarApiClient and CarRepository.
You will need to use mocks to replace those dependencies.

In the setUp we have mocked the CarApiClient dependency using MagicMock.
Try creating a mock for the CarRepository class.
Use these two to initialise CarResolver for this test.

We have added two test cases you should cover - 'test_gets_all_cars' and 
'test_throws_exception_when_manufacturer_is_bankrupt'.

Have a look at the two.
"""

class CarResolverTest(unittest.TestCase):
    def setUp(self):
        # Create a mock for the car API client
        self.car_api_client = MagicMock()

        # Create a mock for the car repository
        # TODO

        # Crate the car resolver with mocked repository and API client
        self.car_resolver = CarResolver(?, ?)

    def test_gets_all_cars(self):
        # Arrange the expected values.
        self.car_api_client.manifacturer_is_not_bankrupt.return_value = True
        # Try setting up the CarRepository find_all_cars method to return 'some cars'.
        # TODO

        # Act
        cars = self.car_resolver.get_all_cars('manufacturer')

        # Assert
        self.assertEqual('some cars', cars)

    def test_throws_exception_when_manufacturer_is_bankrupt(self):
        # Set the expected value of the CarApiClient method 'manifacturer_is_not_bankrupt' to False.
        self.car_api_client.manifacturer_is_not_bankrupt.return_value = False

        # Here we assert that the BankruptManufacturerException is thrown when a non-existing manufacturer is given.
        self.assertRaises(BankruptManufacturerException, self.car_resolver.get_all_cars, 'manufacturer')

