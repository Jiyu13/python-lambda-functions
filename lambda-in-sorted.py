# sorted(iterable, key=key, reverse=reverse)

l = [['red', 'truck'], ['blue', 'truck'], ['red', 'sedan']]

print(sorted(l, key=lambda v: v[1]))    # v: {list: len(list)}(item in list) => each item in the list
# [['red', 'sedan'], ['red', 'truck'], ['blue', 'truck']]

print(sorted(l, key=lambda v: v[1], reverse=True))
# [['red', 'truck'], ['blue', 'truck'], ['red', 'sedan']]
