numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

for num in numbers:
    mod = num % 2
    if mod > 0:
        print(f"{num} is an Odd number.")
    else:
        print(f"{num} is an Even number.")


def 
