import json
from pathlib import Path

# movies = [
#     {"Id": 1, "Title": "Terminator", "Year": 1984},
#     {"Id": 2, "Title": "Kindergarten Cop", "Year": 1990},
# ]

# data = json.dumps(movies)
# Path("movies.json").write_text(data)

# This 'data' is a string. To convert it to a json we use json.loads() method
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[0]["title"])
