def main() :
	import sys

	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT

	def count_divisors(n):
		count = 0
		for i in range(1, n + 1):
			if n % i == 0:
				count += 1
		return count

	def is_anti_prime(n):
		num_divisors = count_divisors(n)
		for i in range(1, n):
			if count_divisors(i) >= num_divisors:
				return False
		return True

	if len(sys.argv) != 2:
		print("Usage: python script.py <positive_integer>")
		return "not anti-prime"

	try:
		num = int(sys.argv[1])
		if num <= 0:
			raise ValueError
	except ValueError:
		print("Please enter a valid positive integer.")
		return "not anti-prime"

	if is_anti_prime(num):
		return("anti-prime")
	else:
		return "not anti-prime"

	## RETURN THE VALUE "anti-prime" or "not anti-prime"

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :
	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main())
