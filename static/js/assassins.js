document.getElementById('namesForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const namesInput = document.getElementById('names').value;
    const names = namesInput.split(',').map(name => name.trim()).filter(name => name);
    
    fetch('/assign', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ names: names })
    })
    .then(response => response.json())
    .then(data => {
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '';
        
        if (data.error) {
            resultsDiv.textContent = data.error;
        } else {
            resultsDiv.innerHTML = '<h2>Assignments:</h2>';
            const list = document.createElement('ul');
            for (const [assassin, target] of Object.entries(data)) {
                const listItem = document.createElement('li');
                listItem.textContent = `${assassin} is assigned to eliminate ${target}.`;
                list.appendChild(listItem);
            }
            resultsDiv.appendChild(list);
        }
    })
    .catch(error => console.error('Error:', error));
});