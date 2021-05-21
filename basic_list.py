def define_list():
    """
    리스트 정의 연슨
    """
    lst1 = list() # 빈 리스트
    print(lst1, type(lst1))
    lst2 = [] # []
    lst3 = [1, 2, "python"]
    print(lst2, lst3)
    lst4 = list("Python") # 다른 시퀀스 객체를 리스트로 반환
    print(lst4)

def list_oper():
    """
    리스트 연산
    순차형의 모든 기능을 수행
    immutable -> 내부 데이터 변경될 수 있다.
    """
    lst = [1, 2, "Python"]

    # 길이 확인
    print(lst, "length:", len(lst))
    # 인덱싱
    print(lst[0], lst[1], lst[2]) # 정인덱싱
    print(lst[-3], lst[-2], lst[-1]) # 역인덱싱

    # Slicing
    print(lst[1:3]) # 항상 경계에 유의
    print(lst[1:]) # 끝 경계 생략 -> 끝까지
    print(lst[:3]) # 시작 경계 생략 -> 처음부터
    print(lst[:]) # 시작 경계, 끝 경계 생략 -> 전체

    print("======================")
    copy = lst[:] # 슬라이싱을 이용한 리스트 전체의 복사
    print(copy)
    print(copy is lst) # 슬라이싱을 이용한 복사 -> 새 객체가 생성된다.

    # 연결(+) -> 원본을 변경시키지 않고 단순히 두 리스트를 연결한 새 리스트를 반환
    #  vs extend : 원본 뒤에 다른 리스트를 연장 -> 내부 데이터 변경
    print(lst + ["Java", True, 3.14159])
    print("원본 : ", lst)

    # append vs extend
    copy.append(["Java", True, 3.14159]) # 전달받은 요소 전체가 index 3에 추가
    print(copy)
    copy.extend(["Java", True, 3.14159]) # 배열 자체를 확장시켜 개별 요소를 하나씩 index에 추가
    print("Extend:", copy)

    # insert
    copy.insert(2, [1, 2, 3]) # 삽입하고 싶은 요소 전체가 index 2에 추가
    print(copy)

    # 반복(*)
    print("원본:", lst)
    print("반복:", lst*3)

    # 포함여부 확인, in, not in
    print("Python" in lst) # lst 리스트에 Python이 포함되어 있는지
    # 인덱스의 확인
    print("INDEX:", lst.index("Python"))

    if "Java" in lst:
        print("INDEX:", lst.index("Java"))

    print("COPY:", copy)

    # 항목의 갯수
    print("COUNT:", copy.count("Python"))

    # 삭제 : del
    del copy[0] # copy의 0번 인덱스 요소 삭제
    print("COPY:", copy)
    # 삭제 : remove
    copy.remove(3.14159)
    print("REMOVE:", copy)

    # 슬라이싱 이용한 치환
    # 메서드 이용보다 슬라이싱 이용 치환 방법 먼저 이용하는 것을 권장
    lst = [1, 12, 123, 1234, 12345]
    print("원본:", lst)
    lst[0:2] = [10, 20]
    print(lst)

    # 슬라이싱 이용한 삭제
    lst[0:2] = [] # 슬라이싱 범위에 빈 리스트를 할당
    print(lst)

    # 슬라이싱 이용한 삽입
    lst[1:1] = ['inserted'] # 중간에 삽입
    print(lst)
    # 맨 마지막에 삽입
    lst[4:] = ["appended"] # 맨 뒤에 삽입
    print(lst)
    # 맨 앞에 삽입
    lst[:0] = ['prepended'] # 맨 앞에 삽입
    print(lst)

     # 다양한 기초 산술 함수 제공
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("SUN:", sum(lst)) # 모든 요소의 합
    print("MIN:", min(lst)) # 최솟값
    print("MAX:", max(lst)) # 최댓값
    print("AVERAGE:", sum(lst)/len(lst)) # 평균 함수는 없다

def list_methods():
    """
    리스트 메서드
    """
    lst = [10, 2, 22, 9, 8,833, 4, 12]
    print("원본: ", lst)
    copy = lst.copy() # 복제 메서드
    print("COPY: ", copy)
    # Reverse : 리스트의 반전
    copy.reverse() # 원본 배열이 변경된다.
    print("REVERSE: ", copy)

    copy = lst.copy()
    print("COPY: ", copy)

    # 정렬 : sort
    # 메서드로서의 sort -> 내부 데이터를 실제 sort
    # 문접적으로서의 sorted -> 정렬된 새 리스트를 반환

    # sorted() 함수
    result = sorted(copy) # copy 리스트를 정렬 후 새 리스트로 반환
    print("SORTED ASC: ", result) # 오름차순 정렬이 기본
    result = sorted(copy, reverse=True) # 내림차순 정렬
    print("SORTED DESC: ", result)

    # 정렬 키 함수 정의
    # 정렬 키 함수를 전달 -> 정렬 기준을 변경
    print("================")
    print("원본: ", copy)
    result = sorted(copy, key=str) # 키 함수를 str로 변경, 해당 정수를 문자열로 변경하고, 그것을 정렬하는 것
    print("SORTED key=str: ", result)

    # 정렬 기준의 사용자 정의
    # 리스트의 요소를 5로 나눈 나머지의 역순으로 정렬 -> 리스트의 ㅇ ㅛ소를 5로 나눈 나머지를 키로 만든다.
    def key_func(val):
        return val % 5
    result = sorted(copy, key=key_func, reverse=True)
    print("SORTED key=custom, DESD: ", result)

    # sort 메서드
    copy.sort(key=key_func, reverse=True)
    print("SORT METHOD: ", copy)

def stack_ex():
    """
    리스트를 활용한 스택의 구현
    append, pop 메서드를 이용한 구현
    Last in, First out
    """
    stack = []
    # 입력
    stack.append(10)
    stack.append(20) # 리스트의 맨 뒤에 요소 입력
    stack.append(30)
    print("STACK:", stack)

    # 인출
    print("POP:", stack.pop())
    print("POP:", stack.pop())
    print("pop:", stack.pop())

    if len(stack): # 스택이 비어있지 않으면
        print("POP:", stack.pop())
    else:
        print("스택이 비어있습니다.")

def queue_ex():
    """
    리스트를 활용한 큐의 구현
    append, pop을 활용 구현
    First in, First out
    """
    queue = []
    # 입력
    queue.append(10)
    queue.append(20)
    queue.append(30)
    print("QUEUE:", queue)

    # 인출
    print("POP:", queue.pop(0)) # 맨 앞에서부터 인출
    print("POP:", queue.pop(0))
    print("POP:", queue.pop(0))
    if len(queue):
        print("POP:", queue.pop(0))
    else:
        print("큐가 비어있습니다.")

def loop():
    """
    리스트의 순회
    """
    words = "Lift is to short, you need Python".replace(",", "").upper().split()
    print(words)

    # 순차자료형은 for ~ in 문으로 차례대로 요소를 전달 받을 수 있다(별도 인덱스 변수는 없다)
    for word in words:
        print("WORD : ", word)



if __name__ == "__main__":
    # define_list()
    list_oper()
    # list_methods()
    # stack_ex()
    # queue_ex()
    # loop()