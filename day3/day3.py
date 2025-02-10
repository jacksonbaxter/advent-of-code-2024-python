import re

def read_input(filename):
    with open(filename, 'r') as file:
        input = file.read()

    return input

def solve_mul(input):
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"

    matches = re.findall(pattern, "".join(input))

    enabled = True
    total = 0

    for matche in matches:
        match matche[0]:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _ if enabled:
                total += int(matche[1]) * int(matche[2])

    return total

def main():
    input = read_input('input.txt')

    answer = solve_mul(input)

    print(f"Multiplications answer: {answer}")

if __name__ == "__main__":
    main()
