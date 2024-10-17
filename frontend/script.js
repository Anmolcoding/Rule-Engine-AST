document.getElementById('create-rule-btn').addEventListener('click', function() {
    const ruleString = document.getElementById('rule-input').value;
    
    fetch('/api/create_rule', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rule: ruleString })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('rule-result').textContent = `Rule created! Rule ID: ${data.rule_id}`;
    })
    .catch(err => {
        document.getElementById('rule-result').textContent = `Error: ${err.message}`;
    });
});

document.getElementById('evaluate-rule-btn').addEventListener('click', function() {
    const ruleId = document.getElementById('rule-id').value;
    const userData = JSON.parse(document.getElementById('user-data').value);
    
    fetch('/api/evaluate_rule', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rule_id: ruleId, data: userData })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('evaluation-result').textContent = `Result: ${data.result}`;
    })
    .catch(err => {
        document.getElementById('evaluation-result').textContent = `Error: ${err.message}`;
    });
});
