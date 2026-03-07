import json
import os

FILE_NAME = "shopping.json"

def load_list():
    """Ielādē sarakstu no JSON faila. Ja faila nav, atgriež tukšu sarakstu."""
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_list(items):
    """Saglabā sarakstu JSON failā."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=4, ensure_ascii=False)