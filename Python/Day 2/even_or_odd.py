question = "What number would you like to check? "
number = int(input(question))
if number % 2 == 0: 
    print(f"{number} is an even number!")
else:    
    print(f"{number} is an odd number!")