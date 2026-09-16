# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")

for i in range(10):
    print(i + 1, "==안녕하세요")

for i in range(1, 10):  # 1 ~ 9
    print(i + 1, "==안녕하세요")

# 1~10
sum = 0
for i in range(1, 11):  # 1 ~ 9
    sum = sum + i
print(sum)
# sum = 0 / i = 1  sum = 0 + 1 / sum = 1
# sum = 1 / i = 2  sum = 1 + 2 / sum = 3
# sum = 3 / i = 3  sum = 3 + 3 / sum = 6
# sum = 6 / i = 4  sum = 6 + 5 / sum = 10

# 짝수의 합 2,4,6,8,10
sum = 0
for i in range(1, 11):  # 1 ~ 9
    if i % 2 != 0:
        sum = sum + i
        print("i => ", i, " / sum => ", sum)
print(sum)

sum = 0
for i in range(2, 11, 2):  # 1 ~ 9
    sum = sum + i
    print("i ====> ", i, " / sum ====> ", sum)
print(sum)
