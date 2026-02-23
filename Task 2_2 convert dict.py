dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

keys_set = set(dct.keys())
print(f"Множество ключей: {keys_set}")

items_set = set(dct.values())
print(f"Множество значений: {items_set}")

summary_set = keys_set.union(items_set)
print(f"Объединение множеств: {summary_set}")
