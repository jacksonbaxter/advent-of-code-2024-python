def read_input(filename):
    with open(filename, 'r') as file:
        pairs = [tuple(map(int, line.strip().split())) for line in file]
        
        left_list = [pair[0] for pair in pairs]
        right_list = [pair[1] for pair in pairs]

    return left_list, right_list

def calculate_total_distance(sorted_left, sorted_right):
    total_distance = 0

    for l, r in zip(sorted_left, sorted_right):
        dis = abs(l - r)
        total_distance += dis

    return total_distance

def calculate_similiarity_score(sorted_left, sorted_right):
    similiarity_score = 0

    for num in sorted_left:
        if num in sorted_right:
            i = sorted_right.index(num)
        else:
            i = -1
        count = 0
        while i < len(sorted_right) and sorted_right[i] == num:
           count += 1 
           i += 1
        similiarity_score += num * count

    return similiarity_score

def main():
    left_list, right_list = read_input('input.txt')

    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)

    total_distance = calculate_total_distance(sorted_left, sorted_right)

    similiarity_score = calculate_similiarity_score(sorted_left, sorted_right)

    print(f"The total distance between the left and the right list is: {total_distance}")

    print(f"The similiarity score is: {similiarity_score}")

if __name__ == "__main__":
    main()
