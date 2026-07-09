import json
import unittest
from fastapi.testclient import TestClient
import os

os.environ["GEMINI_API_KEY"] = "mock-key-for-testing"

from main import app

class TestMain(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok", "service": "invoice-intelligence-extraction"})

if __name__ == "__main__":
    unittest.main()
