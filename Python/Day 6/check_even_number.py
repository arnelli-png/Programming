def check_even(number):
    if number % 2 == 0:
        return True
    else: 
        return False
for number in (4, 11, 3, 55, 100):
    if check_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
