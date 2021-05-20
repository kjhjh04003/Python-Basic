def define_str(): # 문자열의 정의

    # 한 줄 문자열의 정의
    s1 = "Hello Python" # 쌍따옴표(") 홑따옴표(') 모두 가능
    s2 = str("Hello Python") # 타입 함수 이용 생성
    s3 = str(3.14159) # 타 타입을 문자열로 변환환

    print(s1, s2, s3)
    print(type(s1), type(s2), type(s3))

    print("s1은 str의 객체?", isinstance(s1, str))

    # 여러 줄 문자열의 정의
    # 쌍따옴표 세 개("""), 홑따옴표 세개(''')
    s4 = """Life is too short, you need python.
파이썬은 데이터 처리가 중요한 시대에서 가장 널리 사용되는
언어이다.
    """
    print(s4)

    # 여러 줄 문자열은 한 줄 주석만 있는 파이썬에서 여러 줄 주석을 사용하고자 할 때 이용
    # 메서드 정의부 바로 아래 여러 줄 문자여을 입력하면 help 명령어를 이용하여 해당 메서드 주석을 볼 수 있다.
    # -> docstring

def string_oper(): #  문자열 연산
    """
    문자열 연산 연습
    str : len() -> 길이 확인
        연결(+), 반복(*), 포함 여부 확인 가능
        인덱싱, 슬라이싱 가능
        불변자료형(immutable) -> 내부 데이터 변경 불가
    """

    str1 = "Python"
    str2 = "Second String"
    # 길이 : len
    print("str1 length: ", len(str1))

    # 변경 불가 자료형
    #str1[0] = 'f' -> error

    # 인덱싱 : 배열과 비슷하게 인덱스로 접근
    # 인덱스의 범위 : 0 ~ length-1
    print("정인덱싱:", str1[0], str1[1], str1[2], str1[3], str1[4], str1[5])
    print("역인덱싱:", str1[-6], str1[-5], str1[-4], str1[-3], str1[-2], str1[-1])

    # 슬라이싱 : 경계 범위 설정에 유의
    print("[2:4] 슬라이싱", str1[2:4]) # [시작경계:끝경계]
    print("[-4:-2] 슬라이싱", str1[-4:-2]) # 역인덱스 이용한 슬라이싱
    print("[0:3] 슬라이싱:", str1[0:3])
    print("[:3] 슬라이싱:", str1[:3]) # 시작 경계를 생략 -> 처음부터
    print("[3:len(str1)] 슬라이싱:", str1[3:len(str1)])
    print("[3:] 슬라이싱:", str1[3:]) # 끝 경계를 생략 -> 끝까지
    print("[:] 슬라이싱", str1[:]) # 처음부터 끝까지 -> 전체 복제
    # 슬라이싱 [시작경계:끝경계:간격값]
    print("[::2] 슬라이싱", str1[::2]) # 처음부터 끝까지 2간격으로
    print("[::-1] 슬라이싱", str1[::-1]) # 간격이 음수면 방향이 반대

    # 연결(+) -> 산술연산이 아님에 유의
    print(str1 + " Programming")
    # 반복(*)
    print(str1 * 3)

    # 포함 여부 확인 : in, not in
    print("P" in str1)
    print("P" not in str1)

def transform_mathods():
    """
    대소문자 변환 관련 메서드
    """
    s = "i like Python"
    print("원본 : ", s)
    print("UPPER:", s.upper()) # 모두 대문자
    print("LOWER:", s.lower()) # 모두 소문자
    print("SWAPCASE:", s.swapcase()) # 대 <-> 소 문자 변경
    print("CAPITALIZE:", s.capitalize()) # 문장의 첫 글자를 대문자로
    print("TITLE:", s.title()) # 각 단어의 첫글자를 대문자로 변환
    print("원본:", s) # str 객체는 immutable -> 원본 변경되지 않음

def search_methods():
    """
    문자열 검색관련 메서드
    """
    s = "I Like Python, I Like Java Also"
    print("원본 : ", s)
    print("COuNT:", s.count("Like")) # 문자열 내에 Like 갯수
    print("1st Find:", s.find("Like")) # 문자열 내에 Like의 인덱스
    print("2nd Fine:", s.find("Like", 6)) # 6번 인덱스 이후에 Like의 인덱스
    print("3rd Fine:", s.find("Like", 20)) # 없는 검색어는 -1 반환
    print("1st Index:", s.index("Like")) # 문자열 내에 Like 인덱스
    print("2nd Index:", s.index("Like", 6)) # 6번 인덱스 이후에 Like 인덱스
    # print("3rd Index:", s.index("Like", 20)) # 없는 검색어 검색 시 에러
    # 에러 발생시키는 메서드 사용시에는 미리 체크(방어코딩)
    if "Like" in s[21:]: print("3rd Index", s.index("Like", 21))

    print("원본:", s)
    # 역방향 검색 : rfind, rindex
    print("1st RFIND:", s.rfind("Like"))
    print("2nd RFIND:", s.rfind("Like", 0, 17)) # 0~17 인덱스 사이에서 Like 역방향 검색
    # rindex는 검색 결과가 없을 때 ValueError 발생, 이것을 제외하고는 rfind와 사용법 도일

    # 특정 문자열로 시작 or 끝나는가?
    url = "http://www.naver.com"
    surl = "https://www.naver.com"
    ftp = "ftp://ftp.naver.com"

    print("url이 http://로 시작?", url.startswith("http://"))
    print("surl이 https://로 시작?", surl.startswith("https://"))
    # 검색 시 시작 문자열을 여러개 중 한개로 비교하고자 할 때
    print("ftp가 http:// or https://로 시작하는가?", ftp.startswith(("http://", "https://")))
    print("url이 http:// or https://로 시작하는가?", url.startswith(("http://", "https://")))
    print("url이 naver.com으로 끝나는가?", url.endswith("naver.com"))

    # startswith, endwith로 검색 범위를 제한
    print("ftp의 6 ~ 20 영역이 ftp.으로 시작하는가?", ftp.startswith("ftp.", 6, 20)) # 6~20 경계 영역이 ftp.으로 시작하는가

def modify_replace_methods():
    """
    문자열 수정, 치환 관련 메서드
    """
    s = "         Alice and the Hear Queen           "
    print("STRIP:[", s.strip(),"]", sep="") # 앞 뒤의 공백문자 제거
    print("LSTRIP:[", s.lstrip(),"]", sep="") # 왼쪽(앞)의 공백문자 제거
    print("RSTRIP:[", s.rstrip(), "]", sep="") # 오른쪽(뒤)의 공백 문자 제거

    # 기본적으로 String은 공백문자를 제거, 임의의 문자열을 지정하여 제거시킬 수 있다.
    s = "------Alice and the Hear Queen--------"
    print("STRIP -:[", s.strip("-"), "]", sep="") # 앞뒤의 - 문자를 모두 제거

    s = "I Love Java"
    print("원본 : ", s)
    print("REPLACE:", s.replace("Java","Python")) # Java -> Python으로 치환
    print("원본 : ", s) # 원본은 변경되지 않음

def split_join_methods():
    """
    분할과 합치기 메서드
    """

    s = "Ham and Cheese and Breads and Ketchup"
    print("원본 : ", s)
    print("SPLIT:", s.split()) # 기본적으로 공백문자로 분리

    items = s.split(" and ") # 분할 시 " and "기준으로 분리
    print("SPLIT:", items)

    items = s.split(" and ", 2) # " and " 구분자를 기준으로 앞으로부터 2개만 추출하고 나머지는 그냥 출력
    print(items)
    items = s.rsplit(" and ", 2) # " and "구분자를 기준으로 뒤로부터 2개만 추출, 나머지는 그냥 출력
    print(items)

    lines = """
Java Programming
Pythone Programming
Oracle Programming
"""
    print(lines.split()) # 공백문자(스페이스, 개행, 탭) 기준
    print(lines.splitlines()) # 기본적으로는 개행 문자를 유지 안함
    print(lines.splitlines(True)) # True가 들어가면 개행 문자를 삭제 하지 않는다.

def check_method():
    """ 판별 관련 -> is 개옐 메서드 -> bool """
    print("1234567890".isdigit()) # 문자열이 숫자만 포함?
    print("abcdefg".isalpha()) # 문자열이 알파벳만 포함?
    print("Python3".isalnum()) # 문자열이 알파벳+숫자만 포함?
    print("Python 3".isalnum()) # 공백이 포함되어 있어 alnum이 아니다.
    print("\r\n\t".isspace()) # 공백문자만 포함?
    print("".isspace())
    print("PYThON".isupper()) # 전부 대문자인가?
    print("python".islower()) # 전부 소문자인가?
    print("Python Programming".istitle()) # 문자열이 title 형태인가?

def align_mathods():
    """
    문자열 정렬 메서드
    """
    s = "Alice and the Heart Queen"
    print("원본:[", s, "]")
    print("CENTER:[", s.center(60), "]", sep="") # 출력 공간을 60자리 확보하고 중앙정렬, sep는 구분자
    print("CENTER:[", s.center(60, "*"), "]", sep="") # 빈 자리를 *로 채운다.
    print("LJUST:[", s.ljust(60, "*"), "]", sep="") # 왼쪽 정렬
    print("RJUST:[", s.rjust(60, "*"), sep="") # 오른쪽 정렬

    print("ZFILL:", "1234".zfill(5)) # 5자리 확보, 내용을 채운 후 빈자리는 0으로 채운다.
    print("ZFILL:", "1234567890".zfill(5)) # 확보한 자리는 최소공간이고, 자릿수가 넘어가도 내용은 잘리지 않는다.


if __name__ == "__main__":
    # define_str()
    # string_oper()
    # transform_mathods()
    # search_methods()
    # modify_replace_methods()
    # split_join_methods()
    # check_method()
    align_mathods()