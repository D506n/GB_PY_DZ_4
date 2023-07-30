count_bush = int(input("Введите количество кустов: "))
temp_list = []

for step in range(0, count_bush):
    temp_list.append(int(input("Введите количество ягод на кусте: ")))

max_count = []

for step in range(0, count_bush):
    max_count.append(temp_list[step - 2] + temp_list[step - 1] + temp_list[step])

print(max(max_count))