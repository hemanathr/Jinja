from pyjsonata import jsonata

my_expression = "$"
my_json = "{'foo': 'bar'}"
result = jsonata(my_expression, my_json)

# With exception handling:
try:
    result = jsonata(my_expression, my_json)
except PyjsonataError as e:
    print("Error:", e)
