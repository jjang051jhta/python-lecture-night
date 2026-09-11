# 문제 1. 변수 만들기
# 이름, 나이, 키를 각각 변수에 저장하고 출력하세요.
name = "장성호"
age = 23
height = 182
print("이름 :  ", name)
print("나이 : ", age)
print("키 : ", height)

print("이름 :  ", name, "\n나이 : ", age, "\n키 : ", height)

# 2번 풀이
score = 70
score = 90

print("score : ", score)

# 3번
num01 = 20
num02 = 10
print("더하기 : ", (num01 + num02))
print("빼기 : ", (num01 - num02))
print("곱하기 : ", (num01 * num02))
print("나누기 : ", (num01 / num02))
print("나머지 : ", (num01 % num02))
print("제곱 : ", (10**4))


# 4번
name = "홍길동"
age = 20
height = 175.5
is_student = True  # False

print("name의 타입 : ", type(name))
print("age의 타입 : ", type(age))
print("height의 타입 : ", type(height))
print("is_student의 타입 : ", type(is_student))  # boolean

# 5번
age = 20
print("내 나이는 " + str(age) + " 살입니다.")  # type casting  形변환

# 6번
fruits = ["apple", "banana", "mango"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])


# 7번
fruits[1] = "strawberry"
print(fruits)

# 8번
fruits.append("peach")
print(fruits)

name = "abcabcabcabc"
name = name.capitalize()  # "Abc"  str, list
print(name.count("a"))
# class object  객체

# 9번
colors = ("red", "green", "blue")
print(colors[0])
print(colors[1])
print(colors[2])
colors = list(colors)
colors.append("purple")
print(colors)

# 10 번
student = {"name": "홍길동", "age": 20, "score": 85}
print(student["name"])
print(student["age"])
print(student["score"])
