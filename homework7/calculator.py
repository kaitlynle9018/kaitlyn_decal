import math_tools

def main():
	while True:
		print("Welcome to the simple calculator!")
		num1 = input("Enter the first number (or 'q' to quit): ")
		if num1.lower() == 'q':
			print("Naur, don't leave me so soon :<")
			break
		num2 = input("Enter the second number: ")

		try:
			num1 = float(num1)
			num2 = float(num2)
		except ValueError:
			print("Invalid input. Please enter numbers only.")
			continue

		operation = input("Choose an operation (+, -, *, /): ")

		if operation == '+':
			result = math_tools.add(num1,num2)
		elif operation == '-':
			result = math_tools.subtract(num1,num2)
		elif operation == '*':
			result = math_tools.multiply(num1,num2)
		elif operation == '/':
			result = math_tools.divide(num1,num2)
		else:
			print("Invalid operation. Please read directions you buffoon :>, choose +,-,*, or /.")
			continue

		print(f"Result: {result}")

		with open("calc_history.txt", "a") as file:
			file.write(f"{num1} {operation} {num2} = {result}\n")

if __name__ == "__main__":
	main()
