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
# total, maxval, minval, avg = num3_summary(80, 75, 90, 95, 85)
# print(total, maxval, minval, avg)

def q1():
    while True:
        num = input("수를 입력하세요> ")

        try:
            int(num) # 캐스팅 시도
        except: # 캐스팅 실패
            print("정수가 아닙니다. 다시 입력하세요")
        else: # 정상적으로 캐스팅 완료
            break

    total = 0
    to = int(num)
    # for i in range(1, to + 1):
        # if i % 3 == 0:
            # total += i
    lst = [i for i in range(1, to + 1) if i % 3 == 0] # 3의 배수 list
    total = sum(lst)

    print("1부터 {}까지의 3의 배수의 합 = {}".format(to, total))

def q2():
    lst_cleaned = []
    lst = [1, 3.14, 'python', 7, 89.1, 3]
   #  for item in lst:
        # if isinstance(item, (int, float)):
            # lst_cleaned.append(item)
    lst_cleaned = [item for item in lst if isinstance(item, (int, float))]
    print("cleaned : ", lst_cleaned)

def summary(*args):
    total = sum(args)
    return total, max(args), min(args), total / len(args)

def q3():
    total, maxval, minval, avg = summary(80, 75, 90, 95, 85)
    print(total, maxval, minval, avg)

def q4():
# 4. 문자열에서 ',' '.' '\n'을 제거하고 모두 대문자로 변경
# 변경된 소스를 기반으로 단어의 빈도수를 체크
    s = """We encourage everyone to contribute to Python. 
    If you still have questions after reviewing the material
    in this guide, then the Python Mentors 
    group is available to help guide new contributors through the process."""

    # 데이터 정제
    s = s.replace(",", "").replace(".", "").replace("\n", "").upper()
    splits = s.split()
    print("splits:", splits)

    summary = {} # 결과 dict
    for word in splits:
        if word in summary.keys(): #이미 키에 있으면
            summary[word] += 1
        else: # 키가 없으면
            summary[word] = 1
    for key, value in summary.items(): # (key, value) 튜플 반환
        print("{}:{}".format(key, value))

if __name__ == "__main__":
    # num1()
    # num2()
    # num3_summary()
    # q1()
    # q2()
    # q3()
    q4()