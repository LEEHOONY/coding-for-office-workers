# 목록 list, tuple
#사전 dict - dictionary
#집합 set

# list []
print("list")
List_a = [1, 2, 3]
print(List_a)
print(type([1, 2, 3]))
#index(몇번째)는 0부터 시작
print(List_a[0])
print(List_a[1])
print(List_a[2])
#Slice는 리스트를 자른다는 의미 시작:끝(끝은 포함하지 않음)
print(List_a[0:2])
#Append는 리스트에 새로운 항목 추가
List_a.append(4)
print(List_a)
#Remove는 ()안의 리스트를 지우는 역할
List_a.remove(2)
print(List_a)
#Clear는 ()안에 들어있는 데이터를 지우는 역할
List_a.clear()
print(List_a)

#tuple (1, ) -값 생성 후 변경 불가
print("tuple")
tuple_a = (1, 2, 3)
print(tuple_a)
print(type(tuple_a))
# tuple_a.append(4)

#List와 Tuple 차이: 변하면 안되는 데이터 이용시 tuple사용, List는 수정이 가능하기 때문

# Dict (map) {}
# Key & value
dict_a = {
"apple" : "a type of fruits",
"pen" : "a thing to write"
}
print(dict_a)
print(dict_a["apple"])
# edit value
dict_a["pen"] = "something to write"
print(dict_a)

# set set([]) 중복되지않는다
set_a = set([1, 2, 3])
set_b = set([2, 4, 6])
print(set_a)
print(set_b)
# 집합 - 교집합, 하집합, 차집합, 여집합
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)
