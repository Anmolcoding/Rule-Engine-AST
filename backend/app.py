from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection (replace with your connection string if using MongoDB Atlas)
client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))  # Default to local MongoDB
db = client.rule_engine_db
rules_collection = db.rules

# Node class to represent AST
class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value}, left={self.left}, right={self.right})"

# Function to create AST from rule string
def create_rule(rule_string):
    # Simple parsing logic to convert rule string to AST (you can improve this)
    if "AND" in rule_string:
        parts = rule_string.split("AND")
        left = Node("operand", parts[0].strip())
        right = Node("operand", parts[1].strip())
        return Node("operator", "AND", left, right)
    elif "OR" in rule_string:
        parts = rule_string.split("OR")
        left = Node("operand", parts[0].strip())
        right = Node("operand", parts[1].strip())
        return Node("operator", "OR", left, right)
    return Node("operand", rule_string)

# Function to evaluate AST
def evaluate_ast(ast, data):
    if ast.type == "operand":
        # Evaluate the operand against data (e.g., "age > 30")
        expression = ast.value
        return eval(expression.format(**data))
    elif ast.type == "operator":
        if ast.value == "AND":
            return evaluate_ast(ast.left, data) and evaluate_ast(ast.right, data)
        elif ast.value == "OR":
            return evaluate_ast(ast.left, data) or evaluate_ast(ast.right, data)

# API to create a rule and store it in MongoDB
@app.route('/api/create_rule', methods=['POST'])
def create_rule_endpoint():
    data = request.json
    rule_string = data['rule']
    rule_ast = create_rule(rule_string)
    
    # Store rule and its AST in MongoDB
    rule_id = rules_collection.insert_one({"rule": rule_string, "ast": repr(rule_ast)}).inserted_id
    return jsonify({'rule_id': str(rule_id), 'ast': repr(rule_ast)})

# API to evaluate a rule against user data
@app.route('/api/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    data = request.json
    rule_id = data['rule_id']
    
    # Fetch the rule's AST from MongoDB
    rule_data = rules_collection.find_one({"_id": rule_id})
    
    if not rule_data:
        return jsonify({'error': 'Rule not found'}), 404
    
    rule_ast = create_rule(rule_data['rule'])
    user_data = data['data']
    result = evaluate_ast(rule_ast, user_data)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
