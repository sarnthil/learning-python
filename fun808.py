import json
from collections import Counter

def filter_recipes(words):
     with open ("NYC+openrecipes_cleanv1.jsonl") as f:
        for line in f:
            recipe = json.loads(line)
            for word in words:
                if word in recipe['title']:
                    print(recipe['title'])

filter_recipes(['Russian', 'Soup'])
