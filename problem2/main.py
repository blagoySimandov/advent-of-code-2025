def get_ranges():
    with open("input.txt", "r") as f:
        line = f.readline().strip()
    return line.split(",")


def process_range(number_range: str):
    splt = number_range.strip().split("-")
    start_range = int(splt[0])
    end_range = int(splt[1])

    s = 0

    n = 1
    while True:
        double_num = int(str(n) + str(n))
        if double_num > end_range:
            break
        if double_num >= start_range:
            s += double_num
        n += 1

    return s


ranges = get_ranges()  # e.g., ["10-98", "101-105", "109-115", "117-122"]

full_sum = 0
for r in ranges:
    full_sum += process_range(r)

print("full_sum", full_sum)
