n = int(input("Enter number of students: "))
m = int(input("Enter number of subjects: "))

class_total = 0

for i in range(1, n+1):
    print(f"\nStudent {i}")
    total = 0
    for j in range(1, m+1):
        total += float(input(f"Enter score {j}: "))
    avg = total / m
    print(f"Average for Student {i} = {avg:.1f}")
    class_total += avg

print(f"\nClass Average = {class_total / n:.1f}")
