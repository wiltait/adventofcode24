file_path = 'day1/src/input.txt'

def read_and_split_columns(file_path):
    list1, list2 = [], []

    with open(file_path, 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) == 2:
                list1.append(int(columns[0]))
                list2.append(int(columns[1]))
    
    return list1, list2


def calculate_total_distance():
    list1, list2 = read_and_split_columns(file_path=file_path)
    sorted1 = sorted(list1)
    sorted2 = sorted(list2)

    total_difference = sum(abs(a - b) for a, b in zip(sorted1, sorted2))
    return total_difference

result = calculate_total_distance()
print(result)