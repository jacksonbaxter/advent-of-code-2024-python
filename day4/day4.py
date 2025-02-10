def read_input(filename):
    with open(filename, 'r') as file:
        input = file.read().splitlines()

    return input

def part1(input):
    lines = input[:]
    lines.extend(["".join([row[i] for row in input]) for i in range(len(input[0]))])

    def find_diags(grid):
        rows, cols = len(grid), len(grid[0])

        # top-left to bottom-right
        reg_diags = {}

        # from top-right to bottom-left
        anti_diags = {}

        for r in range(rows):
            for c in range(cols):
                key_reg = r - c
                if key_reg not in reg_diags:
                    reg_diags[key_reg] = []
                reg_diags[key_reg].append(grid[r][c])

                key_anti = r + c
                if key_anti not in anti_diags:
                    anti_diags[key_anti] = []
                anti_diags[key_anti].append(grid[r][c])
                
        return reg_diags, anti_diags

    reg_diags, anti_diags = find_diags(input)
    lines.extend(["".join(i) for i in reg_diags.values()])
    lines.extend(["".join(i) for i in anti_diags.values()])

    return sum(line.count("XMAS") + line.count("SAMX") for line in lines)

def main():
    input = read_input('input.txt')

    p1_ans = part1(input)

    print(f"The number of XMAS appearances is: {p1_ans}")

if __name__ == "__main__":
    main()
