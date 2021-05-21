def define_dict():
    """
    사전 생성 연습
    """
    # 빈 사전
    dct = dict()
    print(dct, type(dct))
    # Literal : {}이용
    dct = {"basketball": 5, "baseball": 9}

    # 사전 객체는 순서가 없고 인덱스가 아닌 키를 이용해서 내용에 접근한다.
    dct['volleyball'] = 6
    print(dct)
    # 길이, 포함여부 확인 가능 : 대상은 키 목록을 대상으로 한다.
    # 연결, 반복 지원 안함
    print("LENGTH of dct : ", len(dct))
    print("soccer 키가 있는가?", "soccer" in dct)
    print("baseball 키가 있는가?", "baseball" in dct)

    # 키의 목록, 값의 목록
    print("키의 목록 : ", dct.keys(), type(dct.keys())) # dct.keys() : 내부적으로 set과 비슷
    print("값의 목록 : ", dct.values(), type(dct.values())) # dct.values() : 내부적으로 list와 비슷
    print("키와 값의 쌍 : ", dct.items(), type(dct.items()))

    # 응용
    # 포함 여부는 key를 대상으로 한다
    # 사전의 값의 포함 여부를 확인?

    # dct의 값 중에서 9 값이 포함되어 있는가?
    print("9 in 값 목록?", 9 in dct.values())

    # 키워드 인자를 이용한 사전의 생성
    d1 = dict(key1="value1", key2="value2")
    print(d1, type(d1))

    # 튜플의 리스트를 이용한 사전의 생성
    d2 = dict([('key1', 'value1'), ('key2', 'value2')])
    print(d2, type(d2))

    # 키 목록, 값 목록 있을 떄 -> zip 객체 이용
    keys = ('one', 'two', 'three')
    values = (1, 2, 3, 4) # 값4 는 키의 짝이 없어 생략된다.
    d3 = dict(zip(keys, values))
    print(d3, type(d3))

    # 사전의 키: 변경 불가 객체만 사용 가능
    d4 = {}
    d4[True] = "true"
    d4[10] = 10
    d4['eleven'] = 11
    d4[(10, '홍길동')] = 100

    # list 등 가변 객체는 키로 사용 불가
    # d4[[1, 2, 3]] = 100 -> error

def dict_method():
    """
    사전의 메서드
    """
    dct = {"soccer": 5, "baseball": 9, "volleyball": 6}
    print(dct)
    # 사전의 키 목록 : keys()
    keys = dct.keys()
    print("키 목록 : ", keys, type(keys))
    # dict_keys 역시 순차형 -> 다른 순차형으로 변환 가능
    lst_keys = list(keys) # dict_keys 타입을 list 타입으로
    print(lst_keys, type(lst_keys))

    # 사전의 값의 목록 : values()
    values = dct.values()
    print("값 목록 : ", values, type(values))
    # dict_values 역시 순차형 -> 다른 순차형으로 변환 가능
    lst_values = list(values) # dict_values 타입을 list 타입으로
    print(lst_values, type(lst_values))

    # (키, 값) 쌍튜플의 목록 : items()
    items = dct.items()
    print("(키, 값)의 목록:", items, type(items))
    lst_items = list(items)
    print(lst_items, type(lst_items))
    # 튜플의 리스트 -> 인덱스 접근 가능
    print("KEY:", lst_items[0][0], "VALUE:", lst_items[0][1])
    # 사전 비우기
    dct.clear()
    print(dct)

def using_dict():
    phones = {"둘리": "010-1234-5678", "도우너": "010-9876-5432", "또치": "010-2222-3333"}
    print(phones)

    # 새로운 항목 추가
    phones['고길동'] = "032-1234-5678"
    print(phones)

    # 키에 접근 vs get() 메서드
    print("둘리", phones['둘리'])
    # print("홍길동", phones['홍길동']) # 없는 키에 접근 -> key error발생
    print("홍길동", phones.get('홍길동')) # get 메서드는 없는 키에 접근 -> none 반환
    #get 메서드를 사용하는 이유
    # 1. 키가 없어도 오류 없이 none 값을 받기 위함
    # 2. 기본값 기능이 있어서 none 값을 받고 싶지 않을 떄
    print("홍길동", phones.get('홍길동', '전화 없음')) # 키가 없으면 기본값을 반환

    # 삭제 : del
    del phones['도우너'] # 도우너 키 삭제
    print(phones)
    
    # 값을 가져오며 삭제 : pop
    print(phones.pop('둘리')) # pop()을 하면 값을 반환한 후 그에 대응하는 키값을 삭제한다.
    print(phones)

def loop():
    """
    사전의 순회
    """
    phones = {"둘리": "010-1234-5678", "도우너": "010-9876-5432", "또치": "010-2222-3333"}
    print(phones)

    # 기본적인 순회
    for key in phones:
        print(key + ":" + phones.get(key))
    print() # 개행

    # 사전으로부터 키의 목록을 리스트로 받아온 후 루프
    for key in phones.keys():
        print(key + ":" + phones.get(key))
    print()

    # 키와 값 쌍튜플을 받아와서 언패킹
    for key, value in phones.items():
        print(key + ":" + value)

if __name__ == "__main__":
    # define_dict()
    # dict_method()
    # using_dict()
    loop()