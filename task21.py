from pprint import pprint


students = [
{

    "name": "ali",
    "group": "A",
}]

def group_students(students: list[dict[str, str]]) -> dict[str, list[str] ] :
    groups = {}

    for student in students:
        groups.setdefault(student['group' ], []) .append(student ['name'])

    return groups



result = group_students(students)
pprint(result)