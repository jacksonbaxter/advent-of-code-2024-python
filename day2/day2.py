def read_input(filename):
    with open(filename, 'r') as file:
        reports = file.read().strip().split('\n')

    reports = [list(map(int, line.split())) for line in reports]
    
    return reports

def is_safe_report(levels):
    if len(levels) <= 1:
        return False

    increasing = levels[1] > levels[0]

    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]

        if abs(diff) < 1 or abs(diff) > 3:
            return False
    
        if increasing and diff <= 0:
            return False
        if not increasing and diff >= 0:
            return False

    return True

def safe_with_removal(levels):
    if is_safe_report(levels):
        return True
        
    for i in range(len(levels)):
        modified_level = levels[:i] + levels[i+1:]
        if is_safe_report(modified_level):
            return True
            
    return False

def calculate_safe(reports):
    safe_count = 0
    for report in reports:
        if safe_with_removal(report):
            safe_count += 1

    return safe_count

def main():
    reports = read_input('input.txt')

    safe_count = calculate_safe(reports)

    print(f"The total number of safe reports is: {safe_count}")

if __name__ == "__main__":
    main()
