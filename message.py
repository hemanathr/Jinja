# write_messages.py
# This script generates individual messages to each student and
# also generates a results page listing all the students and their scores.
# The messages are rendered from a template using Jinja2.
# The results page is rendered from another template.

from jinja2 import Environment, FileSystemLoader

max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Inbaraj",  "score": 100},
    {"name": "Hemanath", "score": 77},
    {"name": "Gopinath", "score": 96},
    {"name": "Salman", "score": 67},
    {"name": "Nikilesh", "score": 82},
    {"name": "Naga Arjun", "score": 89},
    {"name": "Dharshan", "score": 98}
]

environment = Environment(loader=FileSystemLoader("templates/"))

# Render individual messages for each student
for student in students:
    filename = f"message_{student['name'].lower()}.txt"
    template = environment.get_template("message.txt")  # template for message
    content = template.render(  # render the template with student details
        student,
        max_score=max_score,
        test_name=test_name
    )
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... wrote {filename}")

# Render a results page listing all the students and their scores
results_filename = "students_results.html"
results_template = environment.get_template(
    "results.html")  # template for results page
context = {
    "students": students,
    "test_name": test_name,
    "max_score": max_score,
}
with open(results_filename, mode="w", encoding="utf-8") as results:
    results.write(results_template.render(context))
    print(f"... wrote {results_filename}")
