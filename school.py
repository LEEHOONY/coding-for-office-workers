# 학교클래스 만들기

class School:

    def __init__(self, name, establish, address):
        self.name = name
        self.establish = establish
        self.address = address

school1 = School("A", "1971", "서울")
school2 = School("B", "1987", "부산")
school3 = School("C", "1976", "광주")

print(school1.name, school1.establish, school1.address)
print(school2.name, school2.establish, school2.address)
print(school3.name, school3.establish, school3.address)
