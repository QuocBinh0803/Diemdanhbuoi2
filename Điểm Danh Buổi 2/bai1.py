def max_in_sliding_window(num_list, k):
    max_values = []
    n = len(num_list)
    for i in range(n - k + 1):
        window = num_list[i:i + k]
        max_values.append(max(window))
    return max_values

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
result = max_in_sliding_window(num_list, k)
print(result)


