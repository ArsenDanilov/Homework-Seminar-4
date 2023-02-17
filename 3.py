from random import randint

list_1 = [randint(0, 10) for i in range (20)]
print(f'\nВывод списка с повторяющимися псевдослучайными числами: {list_1}\n')
# list_1 = set(unique_elements)
unique_elements = set(list_1)

unique_elements = list(unique_elements)


print(f'Вывод списка, состоящего из уникальных значений: {unique_elements}')
