import json

x = '{ "name":"John", "age":30, "city":"New York"}'

# Converter json para python
y = json.loads(x)
print(y['age'])

# Converter python para json
z = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(z)
print(z)
