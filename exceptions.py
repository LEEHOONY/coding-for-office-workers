# exceptions  버그(예외, 예외처리)

# Zero division Error
# 1 / 0

def divide_by(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."
 # try - except 'try'가 나오면 'except 오류명'이 나와야함

# 4 / 2 = 2
print(divide_by(4, 2))
print(divide_by(4, 0))

# 예외 만들기
# Exception
class EvenNumberDivisionError(Exception):
    pass

def divide_by_odd_number(first, second):
    if second % 2 == 0:
        raise EvenNumberDivisionError
    else:
        return first / second
print(divide_by_odd_number(6, 3))
print(divide_by_odd_number(6, 2))
