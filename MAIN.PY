def is_disarium(number):
    num_str = str(number)
    sum_of_powers = 0
    for index in range(len(num_str)):
        digit = int(num_str[index])
        power = index + 1
        sum_of_powers += digit ** power
    return sum_of_powers == number

user_input = int(input("Enter a number: "))
result = is_disarium(user_input)

if result:
    output_message = f"{user_input} is a Disarium number."
else:
    output_message = f"{user_input} is not a Disarium number."

print(output_message)
