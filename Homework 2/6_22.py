x1 = int(input())
y1 = int(input())
const1 = int(input())

x2 = int(input())
y2 = int(input())
const2 = int(input())

solution_found = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if x1 * x + y1 * y == const1 and x2 * x + y2 * y == const2:
            print(x, y)
            solution_found = True
            break
    if solution_found:
        break

if not solution_found:
    print("No solution")