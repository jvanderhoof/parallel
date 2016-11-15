import random
from add import add_array

numbers = []
for num in range(0,10):
    numbers.append(random.sample(range(1, 100), 10))

results = []
for arr in numbers:
    print arr
    results.append(add_array(arr))

# alternatively:
results = []
for arr in numbers:
    with parallel():
        results.append(add(arr))

print results
