# 연산자
num01 = 20
num02 = 3

print(num01 + num02)  # 더하기
print(num01 - num02)  # 빼기
print(num01 * num02)  # 곱하기
print(num01**num02)  # 제곱하기
print(num01 / num02)  # 실수 나누기
print(num01 // num02)  # 정수 나누기 몫이 나옴
print(num01 % num02)  # 나머지 몫을 버리고 나머지만 취함


# input01 = input("숫자를 입력하세요")
# input02 = input("숫자를 입력하세요")
# print(int(input01) + int(input02))


# 참조  reference
fruits = ["apple", "peach", "berry"]
# newFruits = fruits # shallow copy
newFruits = fruits.copy()  # deep copy
newFruits.append("mango")
print(newFruits)
print(fruits)
fruits.append("banana")
print(newFruits)
print(fruits)
num01 = 100
num02 = num01
num01 = 300
print(num01, num02)
# 변수는 값을 복사해서 대입한다.
# 객체 즉 (list,tuple,dict)는 주소값을 넘겨준다.


age = input("나이를 입력하세요   ")
# 만약에 age가 18보다 작다면 미성년자 아니면 성인
if int(age) < 18:
    print("당신은 미성년자입니다.")
else:
    print("당신은 성인입니다.")

# userId = input("아이디를 입력하세요")
# userPw = input("패스워드를 입력하세요")
