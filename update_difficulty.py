import requests
import json
from datetime import datetime

def get_difficulty():
    try:
        response = requests.get('http://xenblocks.io/difficulty')
        data = response.json()
        return data['difficulty']
    except Exception as e:
        print(f"Error fetching difficulty: {e}")
        return None

def update_difficulty_file(difficulty):
    data = {
        'difficulty': difficulty,
        'last_updated': datetime.utcnow().isoformat()
    }
    with open('difficulty.json', 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    difficulty = get_difficulty()
    if difficulty:
        update_difficulty_file(difficulty)
        print(f"Updated difficulty: {difficulty}")
    else:
        print("Failed to update difficulty")
