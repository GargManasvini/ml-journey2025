nums = [1, 2, 3, 4, 5, 6]
squared_even = [x**2 for x in nums if x%2==0]

print(f'Squared even numbers: {squared_even}')

pairs = [('apple', 3), ('banana', 2), ('cherry',1)]
sorted_pairs = sorted(pairs, key=lambda x:x[1])
print(sorted_pairs)