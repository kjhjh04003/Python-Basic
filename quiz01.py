def quiz_01():
    # q1
    str = "Life is too short, You need Python"
    # 문장에 총 몇 개의 알파벳 글자가 사용되었는지 판별
    print("알파벳 갯수는 ", len(str))
    print()
    # 문자열 내의 글자를 모두 소문자로 변경
    print("모두 소문자로 변경 : ", str.lower())
    print()
    # 문자열 내의 공백과 ,를 제거
    print("공백 제거 : ", str.replace(" ", "")) # 공백 제거
    print("콤마 제거 : ", str.replace(",", "")) # 콤마 제거
    print()
    # 문자열을 list 형태로 변환하고 lst 변수에 담기
    lst = list(str)
    print("리스트로 형변환")
    print(lst, type(lst))
    print()
    # lst를 set로 변환하여 chars 변수에 담기
    chars = set(lst)
    print("셋으로 형변환")
    print(chars, type(chars))
    print()
    # chars를 다시 list로 변환하여 lst에 담기
    lst = list(chars)
    # print(lst, type(lst))
    # lst를 알파벳 순으로 정렬하고, 길이를 출력
    print("원본 : ", lst)
    result = sorted(lst)  # 키 함수를 str로 변경, 해당 정수를 문자열로 변경하고, 그것을 정렬하는 것
    print("정렬 : ", result)

def quiz_02():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 리스트 역으로 출력
    print("역순으로 출력", sorted(lst, reverse=True))
    print()
    # 리스트로부터 [4, 5, 6, 7]을 추출하고 slice에 담기
    slice = lst[3:7]
    print("[4, 5, 6, 7] 출력 : ", slice)
    print()
    # slice의 순서를 뒤집기
    print("slice 역순 : ", sorted(slice, reverse=True))
    print()
    # lst의 적절한 부분에 slice를 끼워넣기
    lst[6:6] = slice
    print(lst)

def quiz_03():
    # 사전을 포함한 리스트
    students = [
        {
            "name": "Kim",
            "kor": 80,
            "eng": 90,
            "math": 80
        },
        {
            "name": "Lee",
            "kor": 90,
            "eng": 85,
            "math": 85
        }
    ]
    # 두 학생의 kor, eng, math 합계 점수와 평균을 사전 데이터에 "total", "average" 키 값으로 넣기
    print(students, type(students))
    # 리스트 내 딕셔너리 키값 이용해서 값 추출 : 리스트명[인덱스][키값]
    result1 = students[0]['kor'] + students[1]['kor']
    result2 = students[0]['eng'] + students[1]['eng']
    result3 = students[0]['math'] + students[1]['math']
    hap = result1+result2+result3
    print("AVG : ", hap/3)




if __name__ == "__main__":
    # quiz_01()
    # quiz_02()
    quiz_03()