scores = [85, 90, 100]
result = 0
num_items = 0

for score in scores:
    result += score
    num_items += 1

result /= num_items
print(result)
