lst = list(map(int, input("Введите числа через пробел:\n").split()))
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список элементов без повторений: {new_lst}")