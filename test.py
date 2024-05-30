import unittest
from unittest.mock import patch
import requests

class APITestCase(unittest.TestCase):
    @patch('requests.get')
    def test_failed_request(self, mock_get):
        # Konfigurasi mock untuk mengembalikan None (tidak ada respons)
        mock_get.return_value = None

        base_url = "https://reqres.in"
        endpoint = "/api/nonexistent_endpoint"
        url = base_url + endpoint

        try:
            response = requests.get(url)
            if response is None:
                print("Permintaan API gagal: tidak ada respons")
        except requests.exceptions.RequestException as e:
            print(f"Kesalahan terjadi saat membuat permintaan: {e}")

if __name__ == "__main__":
    unittest.main()
