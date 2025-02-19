from collections import defaultdict

def read_input(filename):
    with open(filename, 'r') as file:
        input = file.read().strip().split('\n')
    return input

def extract_data(input):
    _sep = input.index("")

    rules = defaultdict(set)
    for i in input[:_sep]:
        a, b = map(int, i.split("|"))
        rules[a].add(b)

    updates = [list(map(int, i.split(","))) for i in input[_sep + 1 :]]
    return rules, updates

def is_valid(rules, update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[j] not in rules[update[i]]:
                return False
    return True

def part1(input):
    rules, updates = extract_data(input)
    count = 0

    for update in updates:
        if is_valid(rules, update):
            count += update[len(update) // 2]

    return count

def main():
    input = read_input('input.txt')

    p1_ans = part1(input)

    print(f"Middle page count: {p1_ans}")

if __name__ == "__main__":
    main()
