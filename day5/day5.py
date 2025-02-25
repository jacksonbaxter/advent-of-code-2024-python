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

def fix_update(rules, update):
    filtered_rules = defaultdict(set)
    for i in update:
        filtered_rules[i] = rules[i] & set(update)

    ordered_keys = sorted(filtered_rules, key = lambda k: len(filtered_rules[k]), reverse = True)

    return ordered_keys

def part1(input):
    rules, updates = extract_data(input)
    count = 0

    for update in updates:
        if is_valid(rules, update):
            count += update[len(update) // 2]

    return count

def part2(input):
    rules, updates = extract_data(input)
    count = 0

    for update in updates:
        if not is_valid(rules, update):
            fixed_update = fix_update(rules, update)
            count += fixed_update[len(update) // 2]

    return count

def main():
    input = read_input('input.txt')

    p1_ans = part1(input)
    p2_ans = part2(input)

    print(f"Middle page count: {p1_ans}")
    print(f"Part 2 middle page count: {p2_ans}")

if __name__ == "__main__":
    main()
