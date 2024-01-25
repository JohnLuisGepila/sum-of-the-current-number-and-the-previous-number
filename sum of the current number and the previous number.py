def sum_of_current_and_previous(current, previous):
    return current + previous

current_number = 0
previous_number = 0

for i in range(1, 11):
    if i == 1:
        current_number = int(input('Enter the first number:'))
        previous_number = current_number
        print("your current number is:", previous_number)
        print("Sum:", current_number)
        continue
    current_number =int(input("Enter the second number:"))
    print("your current number is:", previous_number)
    result = sum_of_current_and_previous(current_number, previous_number)
    print("Sum: ", result)
    previous_number = current_number