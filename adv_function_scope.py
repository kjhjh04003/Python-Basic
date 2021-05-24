# 함수 스코핑 룰
x = 1 # Global

def scope_func(a):
    return a + x # local 스코프에 x가 없음 -> 함수 밖에 선언된 글로벌x를 참조

def scope_func2(a):
    x = 2 # 치환 -> 로컬 스코프에 x 심볼이 생성 -> 글로벌x가 아니라는 것
    return a + x # local 스코프 a, local 스포트 x 합산

print(scope_func(10))
print(scope_func2(10))
print("global x : ", x) # scope_func2에서 x가 치환되었지만, global x에 영향을 미치지 않는다.

g = 1 # 글로벌 변수

def scope_func3(a):
    # 함수 내부에서 전역 객체를 사용해야 한다 -> global 키워드를 사용
    global g
    g = 3
    return a + g

print(scope_func3(10))
print("global g:", g)

# 글로벌 영역 확인
print(dir())
# 내장 영역의 확인
print(dir("내장영역: ", '__builtins__'))