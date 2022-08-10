# 클래스 생성
class Human:
    name = "Bob"
    age = 10
    def exercise(self):
        print("스쿼시!")

# 필드: 객체가 가지고 있는 성질 = 겍체가 가지고 있는 변수 (name, age)
# 메서드: 객체가 할 수 있는 행동 = 객체가 할 수 있는 함수 (def~)

## self: 메서드라면 가져야 하는 첫번째 매개변수.

# 인스턴스: 객체를 만들 수 있는 틀(클래스)로 찍어낸 객체

bobby = Human()
bobby.name # Bob
bobby.age # 10

# 인스턴스 매서드()
bobby.exercise()
