import unittest
from app import create_rule, evaluate_ast

class RuleEngineTest(unittest.TestCase):
    def test_create_rule(self):
        rule_string = "age > 30 AND salary > 50000"
        rule_ast = create_rule(rule_string)
        self.assertIsNotNone(rule_ast)

    def test_evaluate_ast(self):
        rule_string = "age > 30 AND salary > 50000"
        rule_ast = create_rule(rule_string)
        user_data = {"age": 35, "salary": 60000}
        result = evaluate_ast(rule_ast, user_data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
