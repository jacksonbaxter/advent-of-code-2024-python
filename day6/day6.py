def read_input(filename):
    with open(filename, 'r') as file:
        return [line.rstrip() for line in file.readlines()]

def get_guard_pos(_map):
    rows, cols = len(_map), len(_map[0])
    for i in range(rows):
        for j in range(cols):
            if _map[i][j] == "^":
                return (i, j)

def patrol(_map, pos = None, idx = None):
    if not pos:
        pos = get_guard_pos(_map)

    if not idx:
        idx = 0

    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    rows, cols = len(_map), len(_map[0])

    visited = set()
    visited.add((pos[0], pos[1]))

    visited_entry = {}

    while True:
        d = directions[idx]
        n = (pos[0] + d[0], pos[1] + d[1])

        if n[0] < 0 or n[0] >= rows or n[1] < 0 or n[1] >= cols:
            return True, visited, visited_entry
        
        if _map[n[0]][n[1]] == "#":
            idx = (idx + 1) % 4
            continue
        else:
            visited.add((n[0], n[1]))
            if n not in visited_entry:
                visited_entry[n] = (pos, idx)
            elif visited_entry[n] == (pos, idx):
                return False, None, None # found loop
            pos = n

def part1(input):
    _map = [list(line) for line in input]
    is_leaving, visited, visited_entry = patrol(_map)

    return len(visited)

def main():
    input = read_input('input.txt')

    p1_ans = part1(input)

    print(f"Number of distinct positions: {p1_ans}")

if __name__ == "__main__":
    main()
