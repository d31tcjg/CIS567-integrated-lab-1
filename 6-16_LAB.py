# Get inputs
first_int = int(input())
second_int = int(input())

# Check if the second integer is less than the first
if second_int < first_int:
    print("Second integer can't be less than the first.")
else:
    # Output range with increments of 5
    current = first_int
    while current <= second_int:
        print(current, end=" ")
        current += 5
    print()  # Newline at the end
