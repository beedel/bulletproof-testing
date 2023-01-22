import unittest

from src.CarApiClient import CarApiClient

"""
This is the test class for CarApiClient.

In the setUp method we initialise the original class. It has no dependencies, so no mocks are used.

We have added a 'happy' test case scenario - 'test_manufacturer_is_not_bankrupt'.

Look at the CarApiClient class.

Can you find any 'failure' cases that you need to cover?

Are there any exceptions that you should ensure are thrown during code execution? In what case are they thrown?

Try to write additional test cases to cover as much of the CarApiClient class as possible.
"""


class CarApiClientTest(unittest.TestCase):
    def setUp(self):
        # Initialise the API client
        self.car_api_client = CarApiClient(self)

    def test_manufacturer_is_not_bankrupt(self):
        # Arrange
        expected = True

        # Act
        connected = self.car_api_client.manifacturer_is_not_bankrupt('Ford')

        # Assert
        self.assertEqual(expected, connected)


if __name__ == '__main__':
    unittest.main()
