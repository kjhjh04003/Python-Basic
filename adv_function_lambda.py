# Lambda 함수 : 이름이 없는 익명 함수
def square(x):
    return x ** 2

for i in range(10): # 0~9까지 반복
    print("{}:{}".format(i, square(i)), end = " ")
else:
    print()

# lambda 식으로 교체
for i in range(10):
    print("{}:{}".format(i, (lambda x: x ** 2)(i)), end = " ") # 즉시 실행 lambda
else:
    print()

# lambda를 이용한 sort 키함수 정의
strings = "Life is too short, you need Python".upper().replace(",","").split()
print("STRINGS:",strings)
# 문자열을 길이를 기준으로 역순정렬
def strlen(x):
    return len(x)
# result = sorted(strings, key = strlen, reverse = True)
result = sorted(strings, key = lambda x: len(x), reverse = True)
print("LEN DESC : ", result)

# lambda 식으로 교체
