# 포켓몬 클래스 생성
# 특징: 이름, 체력, 타입, 도감번호 등
# 능력: 기술(울음소리, 백만볼트 등등)

class Poxxmon:
    p_name = ""
    p_hp = 0

class Pixxchu(Poxxmon):
    p_name = "Pixxchu"
    p_hp = 50
    p_type = "Electric"

    def skill(self):
        print("10만 볼트!")

pixx = Pixxchu()
pixx.skill()
print(pixx.p_hp)

# 왜 객체지향 프로그래밍인가?
# 상속, 다형성, 캡슐화를 통해 코드의 재사용이 쉽고, 우리 실생활을 더 잘 나타낼 수 있다.

