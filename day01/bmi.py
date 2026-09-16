# 키(cm)와 몸무게(kg)를 입력받아서 비만도 테스트를 해보세요.
# BMI = 몸무게(kg) / (키(m) × 키(m))
# BMI	판정
# 18.5 미만	저체중
# 18.5 이상 ~ 23 미만	정상
# 23 이상 ~ 25 미만	과체중
# 25 이상	비만
height = int(input("키를 cm입력하세요. "))
weight = int(input("몸무게를 kg입력하세요."))
cm = height / 100
bmi = weight / (cm * cm)
print("당신의 체질량 지수는 : ", bmi)
if bmi < 18.5:
    print("저체중")
elif bmi >= 18.5 and bmi < 23:
    print("정상")
elif bmi >= 23 and bmi < 25:
    print("과체중")
else:
    print("비만")
