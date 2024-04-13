# 定义一个函数，将输入的数字加倍
def double(x):
    return x * 2

# 定义一个列表
numbers = [1, 2, 3, 4, 5]

# 使用 map() 函数将 double 函数应用于 numbers 中的每个元素
result = map(double, numbers)

# 打印结果，注意这是一个迭代器
print(result)  # 输出 <map object at 0x7f9b65d4c550>

# 将迭代器转换为列表
result_list = list(result)

# 打印转换后的列表
print(result_list)  # 输出 [2, 4, 6, 8, 10]
