numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} # 전체 집합
evens = {0, 2, 4, 6, 8} # 짝수 집합
odds = {1, 3, 5, 7, 9} # 홀수 집합
mthree = {0, 3, 6, 9} # 3의 배수 집합

def define_set():
    """
    SET 정의 연습
    set() 함수
    {}
    """
    empty = set() # 빈 집합 생성
    print(empty, type(empty))
    empty={} # 주의 : 빈 SET가 아니라 빈 사전
    print(empty, type(empty))

    # 순서가 없고, 인덱스도 없고, 슬라이싱도 안된다.
    # 길이(요소의 수), 포함 여부(in, not in) 정도만 사용 가능
    print(numbers, "LENGTH:", len(numbers))
    print("포함 여부 : ", 2 in numbers, 2 in evens, 2 in odds)

    # 캐스팅 : 다른 순차형으로 set 만들기
    s = "Python Programming" # 문자열 안쪽에 모두 몇 개의 알파벳이 사용되었는지
    chars = set(s.upper()) # 중복 제거, 순서 없다.
    print(s, chars)

    # 중복 허용 안함 특성
    # list 등의 중복값 제거에 유용
    lst = "Python Programming Java Programming".upper().split()
    print(lst)
    words = set(lst)
    print(words, len(words))

def set_methods():
    """
    set의 메서드
    """
    print("전체 집합 : ", numbers)
    # 요소의 추가
    numbers.add(10) # 10 요소를 추가
    print("전체 집합 : ", numbers)
    evens.add(10)
    print("짝수 집합 : ", evens)
    evens.add(4) # 이미 있는 값을 추가할 경우, 중복이 되기 때문에 새롭게 추가되지 않는다.
    print("짝수 집합 : ", evens)
    # 삭제: discard, remove
    evens.discard(4)
    print("짝수 집합 : ", evens)
    evens.discard(4) # discard -> 없는 요소를 삭제해도 에러 발생 안함
    # evens.remove(4) # remove -> 없는 요소를 삭제하면 KeyError 발생
    # 집합 업데이트
    evens.update({2, 4, 6}) # 중복되지 않은 값만 삽입
    print("짝수 집합 : ", evens)

def set_oper():
    """
    집합 연산
    교집합, 합집합, 차집합
    판별 연산
    모집합 여부, 부분 집합 여부
    """
    # 짝수 집합 합집합 홀수집합 == 전체집합
    print(evens.union(odds) == numbers)
    print("짝수 합집합 홀수 : ", evens | odds == numbers)

    # 모집합, 부분집합 판별
    print("전체집합이 짝수 집합의 모집합?", numbers.issuperset(evens))
    print("홀수집합이 전체집합의 부분집합?", odds.issubset(numbers))

    # 교집합
    print("짝수 교집합 3의배수:", evens.intersection(mthree))
    print(mthree & odds == {3, 9})

    # 차집합
    print("전체 차집합 짝수:", numbers.difference(evens))
    print("전체 차집합 짝수 -> 홀수?", numbers-evens == odds)


if __name__ == "__main__":
    # define_set()
    # set_methods()
    set_oper()