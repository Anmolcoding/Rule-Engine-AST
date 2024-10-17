import unittest
from app import app

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_rule(self):
        response = self.app.post('/api/create_rule', json={'rule': 'age > 30 AND salary > 50000'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('rule_id', response.get_json())

    def test_evaluate_rule(self):
        # Assuming a valid rule_id from above test
        rule_id = "some_existing_rule_id"
        response = self.app.post('/api/evaluate_rule', json={'rule_id': rule_id, 'data': {"age": 35, "salary": 60000}})
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.get_json())

if __name__ == '__main__':
    unittest.main()
