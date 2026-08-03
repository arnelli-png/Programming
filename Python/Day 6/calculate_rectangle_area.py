def calculate(length, width):
    return length * width 

for length, width in [(5, 4), (5, 7), (9, 8)]:
    area = calculate(length, width)
    print(f"The area is: {area}") 


