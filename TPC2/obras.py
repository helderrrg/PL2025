import sys

def obras():
    lines = sys.stdin.readlines()
    
    full_lines = []
    current_line = ""
    x = 100

    for line in lines:
        line = line.strip()
        current_line += line

        semicolon_count = current_line.count(';')
        print(semicolon_count)
        print(current_line)

        x -= 1
        if x == 0:
            break

        if semicolon_count == 6:
            full_lines.append(current_line)
            current_line = ""

    composers = set()
    works_by_period = {}
    period_titles = {}

    for line in full_lines[1:]:
        columns = line.split(';')
        
        if len(columns) < 7:
            continue
        
        title, desc, year, period, composer, duration, _id = columns

        composers.add(composer.strip())

        if period not in works_by_period:
            works_by_period[period] = 0
            period_titles[period] = []

        works_by_period[period] += 1
        period_titles[period].append(title.strip())

    sorted_composers = sorted(composers)

    for period in period_titles:
        period_titles[period].sort()

    print("Lista ordenada de compositores:")
    print(sorted_composers, "\n")
    print("\nDistribuição das obras por período:")
    print(works_by_period, "\n")
    print("\nDicionário de títulos por período:")
    print(period_titles, "\n")

if __name__ == "__main__":
    obras()
