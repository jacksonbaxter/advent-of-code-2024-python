def read_input(filename):
    with open(filename, 'r') as file:
        pairs = [tuple(map(int, line.strip().split())) for line in file]
        
        left_list = [pair[0] for pair in pairs]
        right_list = [pair[1] for pair in pairs]

    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)

    total_distance = 0

    for l, r in zip(sorted_left, sorted_right):
        dis = abs(l - r)
        total_distance += dis

    return total_distance


def main():
    left_list, right_list = read_input('input.txt')

    result = calculate_total_distance(left_list, right_list)

    print(f"The total distance between the left and the right list is: {result}")

if __name__ == "__main__":
    main()
