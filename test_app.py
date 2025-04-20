import unittest
from app import app

class TestFeedbackApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_page(self):
        response = self.app.get('/dashboard')
        self.assertEqual(response.status_code, 200)
