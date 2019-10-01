# tool analyzes provided numbers

numbers = []
total = 0
lowest = None
highest = None

while True:
    try:
        line = input("enter a number or Enter to finish: ")
        if not line:
            break
        number = int(line)
        numbers.append(number)
        total += number
        if lowest is None or lowest > number:
            lowest = number
        if highest is None or highest < number:
            highest = number
    except ValueError as err:
        print(err)

print("numbers: ", numbers)
print(
    "count=",
    total,
    "; lowest=",
    lowest,
    "; highest=",
    highest,
    "; mean=",
    total / len(numbers),
)
