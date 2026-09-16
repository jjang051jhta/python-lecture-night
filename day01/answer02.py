# 1 사용자로부터 정수 하나를 입력받으세요. 입력한 숫자가 0보다 크면 "양수입니다."를 출력하세요.
num = input("정수를 입력하세요.")  #   "10"
if int(num) != 0:
    print("양수입니다.")
else:
    print("음수입니다.")

# > 크다  <  작다  >= 크거나 같다  <= 작거나 같다  == 같다 != 다르다

# 2 나이를 입력받아 18세 이상이면 "성인입니다.",
# 그렇지 않으면 "미성년자입니다."를 출력하세요.
age = input("나이를 입력하세요")
if int(age) >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# 3 정수를 입력받아 짝수인지 홀수인지 출력하세요.
num = input("정수를 입력하세요.")
if int(num) % 2 == 0:
    print("even 짝수")
else:
    print("odd 홀수")

# 4 두 개의 정수를 입력받아 더 큰 숫자를 출력하세요.
num01 = int(input("정수를 입력하세요."))
num02 = int(input("정수를 입력하세요."))
if num01 > num02:
    print("큰 숫자는 ", num01, "입니다.")
else:
    print("큰 숫자는 ", num02, "입니다.")

# 5 점수를 입력받아 다음 기준으로 학점을 출력하세요.
# 90점 이상	A
# 80점 이상	B
# 70점 이상	C
# 60점 이상	D
# 60점 미만	F
score = int(input(" 점수를 입력하세요."))
# if score >= 90:
#     print("A")
# if score >= 80 and score < 90:
#     print("B")
# if score >= 70 and score < 80:
#     print("C")
# if score >= 60 and score < 70:
#     print("D")
# if score < 60:
#     print("F")

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# 6 다음 두 조건을 모두 만족하면 "로그인 성공"을 출력하세요.
userId = input("아이디를 입력하세요.")
userPw = input("패스워드를 입력하세요.")
if userId == "admin" and userPw == "1234":
    print("로그인 성공")
else:
    print("로그인 실패")

# 7 다음 조건 중 **하나라도 만족하면** `"할인 대상입니다."`를 출력하세요.
# - 13세 이하
# - 65세 이상
age = int(input("나이를 일력하시면 할인대상자인지 알려드립니다."))
if age <= 13 or age >= 65:
    print("할인대상입니다.")
else:
    print("할인대상이 아닙니다.")

# 8 서로 다른 정수 3개를 입력받아 가장 큰 숫자를 출력하세요.
num01 = int(input("첫번째 숫자를 입력하세요."))
num02 = int(input("두번째 숫자를 입력하세요."))
num03 = int(input("세번째 숫자를 입력하세요."))
if num01 > num02 and num01 > num03:
    print("제일 큰 숫자는 ", num01, "입니다.")
elif num02 > num01 and num02 > num03:
    print("제일 큰 숫자는 ", num02, "입니다.")
else:
    print("제일 큰 숫자는 ", num03, "입니다.")

# 9  연도를 입력받아 윤년인지 아닌지 판별하세요.
# 4로 떨어지면 윤년 100으로 떨어지면 윤년 아님
# 400 으로 떨어지면 윤년
year = int(input("년도를 입력하세요."))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("윤년 leaf year")
else:
    print("평년 non leaf year")

# 10 두 개의 숫자와 연산자를 입력받아 계산 결과를 출력하세요.

# 사용할 수 있는 연산자는 다음과 같습니다.

# - + : 더하기
# - : 빼기
# - : 곱하기
# - / : 나누기
num01 = int(input("첫번째 숫자를 입력하세요."))
operator = input("연산자를 입력하세요. ( +,-,*,/ )")
num02 = int(input("두번째 숫자를 입력하세요."))

if operator == "+":
    print(num01 + num02)
elif operator == "-":
    print(num01 - num02)
elif operator == "*":
    print(num01 * num02)
elif operator == "/":
    if num02 == 0:
        print("0으로 나눌 수 없습니다.")
    else:
        print(num01 / num02)
else:
    print("지원하지 않는 연산자입니다.")
