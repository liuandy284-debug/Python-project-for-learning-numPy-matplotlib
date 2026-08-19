grades = {"Andy": 95, "Bob": 72, "Carol": 88, "Sam": 60, "Lily": 91}
new_dic = {}
notified = set()
print("==============================")
for name, grade in grades.items():
    print(f"Name: {name}, grade: {grade}")
    if(grade > 80):
        new_dic[name] = grade
        notified.add(name)   # list use append, set use add
print("==============================")
print(notified)
print("==============================")

def get_grade(name):   #define a standard of comparsion
    return grades[name]

best = max(grades, key = get_grade)  #using key to customize the
print(f"Best score in the class: {best}")
print("==============================\n")
print("Ranked score: ")
ranked = sorted(grades, key = get_grade, reverse = True)
for i, name in enumerate(ranked):
    print(f"{i + 1}: {name} ")