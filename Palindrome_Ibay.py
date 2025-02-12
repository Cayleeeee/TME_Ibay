def is_palindrome(n):
    return str(n) == str(n)[::-1]

try:
    with open("numbers.txt", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            numbers = list(map(int, line.strip().split(",")))
            total = sum(numbers)
            status = "Palindrome" if is_palindrome(total) else "Not a palindrome"
            print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {status}")
except FileNotFoundError:
    print("Error: File 'numbers.txt' not found.")
