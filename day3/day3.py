import re

def read_input(filename):
    with open(filename, 'r') as file:
        input = file.read()

    return input

def solve_mul(input):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

    matches = re.finditer(pattern, input)

    total = 0
    for match in matches:
        x, y = map(int, match.groups())
        total += x * y

    return total

def main():
    input = read_input('input.txt')

    answer = solve_mul(input)

    print(f"Multiplications answer: {answer}")

if __name__ == "__main__":
    main()
