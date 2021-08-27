# 统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1,
# -9, -4, -5, 8]

d = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]

# 方法一
# 正数
res = [i for i in d if i<0 ]
print(res)

# 负数
f_res = [i for i in d if i > 0]
print(f_res)

# 方法二
z_res = []
f_res = []
for i in d:
    if i < 0:
        z_res.append(i)
    elif i > 0:
        f_res.append(i)
print('正数：',z_res)
print('负数：',f_res)


# 字符串 "axbyczdj"，如果得到结果“abcd”
a = "axbyczdj"
print(a[::2])

c = []
for i in range(len(a)):
    if i%2 ==0:
        c.append(a[i])
print("".join(c))

