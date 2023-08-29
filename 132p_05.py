#02-3 변수와 입력 132p 05번
str_input = input("원의 반지름입력 > ")
num_input = float(str_input)
print()
print("반지름: ", num_input)
print("둘레: ", 2 * 3.14 * num_input)
print("넓이: ", 3.14 * num_input ** 2)