def average(scores):
    result1 = sum(scores)/len(scores)
    return result1

def classify(result1):
    if result1>=80:
        return "Distinction"
    elif result1>=60:
        return "First Class"
    else:
        return "Fail"
def topper(students):
    topper_name = None
    topper_score = 0

    for student in students:
        avg= average(student["Scores"])
        if(avg>topper_score):
            topper_score = avg
            topper_name = student["name"]
    return topper_name


    
students = [
    {"name":"Alice", "Scores":[85,65,78]},
    {"name":"Elsa", "Scores":[87,75,88]},
    {"name":"Nikita", "Scores":[89,95,78]}
]


for student in students:
    avg = average(student["Scores"])
    # print(f"{avg:.2f}")
    # print(classify(avg))
    print(f"{student['name']} | Avg: {avg:.2f} | {classify(avg)}")

print(f"Topper: {topper(students)}")