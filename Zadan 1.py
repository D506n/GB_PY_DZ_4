def input_list(max_count, name):
    temp_list = []
    step = 0
    while step < max_count:
        temp_list.append(int(input(f"Введите {step+1} элемент {name} множества: ")))
        step += 1
    return temp_list

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

n_list = input_list(n, "первого")
m_list = input_list(m, "второго")

n_list = set(n_list)
m_list = set(m_list)

result = n_list.intersection(m_list)
result = list(result)
result.sort()
print(result)