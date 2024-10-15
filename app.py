from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')




@app.route('/assassins')
def assassins():
    return render_template('assassins.html')

@app.route('/assassins_assign', methods=['POST'])
def assign():
    names = request.json.get('names', [])
    try:
        assignments = assign_targets(names)
        return jsonify(assignments)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

def assign_targets(names):
    """Assign each person in the list to another in a circular fashion for a game of assassins."""
    if len(names) < 3:
        raise ValueError("At least 3 players are required to play the game.")
    
    shuffled_names = names.copy()
    random.shuffle(shuffled_names)
    
    assignments = {}
    num_players = len(shuffled_names)
    for i in range(num_players):
        assassin = shuffled_names[i]
        target = shuffled_names[(i + 1) % num_players]  # Circular assignment
        assignments[assassin] = target
    return assignments

if __name__ == '__main__':
    app.run(debug=True)
