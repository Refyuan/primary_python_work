fibonacci=[1,1]
for i in range(2,9999):
    fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
user_input=input("输入整数n=")
try:
    n=int(user_input)
    print(f"第n项为{fibonacci[n-1]}")
except ValueError:
    print("输入错误，请输入整数")
