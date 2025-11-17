import unittest
from app import app

class appTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

    def test_convert_01(self):
        request_body = {"amount": 100, "from":"USD", "to":"ILS"}
        response = self.client.post("/convert", json=request_body)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["converted"], 370.0)

    def test_convert_02(self):
        request_body = {"amount": 100, "from":"EUR", "to":"ILS"}
        response = self.client.post("/convert", json=request_body)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(response.get_json()["converted"]), 402)
    


if __name__ == "__main__":
    unittest.main()
