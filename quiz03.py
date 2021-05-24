# 1. 키보드로 정수를 입력받는다.
# 입력받은 값이 정수 형태가 아니면 "정수가 아닙니다"를 출력
# 입력받은 값이 정수라면 1부터 해당 입력값까지의 정수 중에서 3의 배수만 합산하여 출력
def num1():
    result = 0
    while True:
        try:
            num = int(input("수를 입력하세요:"))
            if isinstance(num, int):
                for i in range(1, num+1):
                    if(i%3==0):
                        result += i
                print("1부터 ", num,"까지 3의 배수의 합 = ", result)
                break
        except Exception as e:
            print("정수가 아닙니다. 다시입력하세요")
            print()

# 2. lst = [1, 3.14, 'python', 7, 89.1, 3]
# 해당 리스트에서 정수형, 실수형 데이터만 추출하여 lst_cleaned라는 이름의 리스트에 담기
def num2():
    lst_cleaned = []
    lst = [1, 3.14, 'python', 7, 89.1, 3]

    for item in lst:
        if isinstance(item, (int,float)):
            lst_cleaned.append(item)
    print(lst_cleaned)

# 3. 메서드를 하나 만들고, 임의의 개수의 인수를 받아서 해당 인수의 합, 최대값, 최소값, 평균값을
# 한꺼번에 반환하는 함수 만들기
def num3_summary(*args):
    total, maxval, minval, avg = 0
    for i in args:
        total += i
        maxval = max(args)
        minval = min(args)
        avg = total / len(args)
    return total, maxval, minval, avg
print(num3_summary(10, 20, 30, 40, 50), type(num3_summary(10, 20, 30, 40, 50)))
# total, maxval, minval, avg = num3_summary(80, 75, 90, 95, 85)
# print(total, maxval, minval, avg)

# if __name__ == "__main__":
    # num1()
    # num2()
    # num3_summary()