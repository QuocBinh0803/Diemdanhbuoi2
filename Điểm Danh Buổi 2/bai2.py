def max_in_sliding_window(num_list, k):
    max_values = []
    n = len(num_list)
    for i in range(n - k + 1):
        window = num_list[i:i + k]
        max_values.append(max(window))
    return max_values
def input_num_list():
    num_list = []
    while True:
        num = input("Nhập số nguyên (nhập 'done' để kết thúc): ")
        if num.lower() == 'done':
            break
        try:
            num_list.append(int(num))
        except ValueError:
            print("Vui lòng nhập một số nguyên hoặc 'done' để kết thúc.")
    return num_list
def input_window_size():
    while True:
        k = input("Nhập kích thước cửa sổ trượt (k > 0): ")
        try:
            k = int(k)
            if k > 0:
                return k
            else:
                print("Kích thước cửa sổ trượt phải là một số nguyên dương.")
        except ValueError:
            print("Vui lòng nhập một số nguyên dương.")
num_list = input_num_list()
k = input_window_size()
result = max_in_sliding_window(num_list, k)
print("Các giá trị lớn nhất trong cửa sổ trượt là:", result)
