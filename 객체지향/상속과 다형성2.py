class Reaction:
    def __init__(self, type, post, user):
        self.type = type
        self.post = post
        self.user = user

class Like(Reaction):#(reaction을 상속받도록)
    def __init__(self, post, user):
        super().__init__("LIKE", post, user)
        #내가 받은 매개변수를 -> 부모.인자로 넘겨준다.

class Sad(Reaction):
    def __init__(self, post, user):
        super().__init__("SAD", post, user)
    
# 이렇게 쓰진 않는다!
# reaction = Reaction("vasdfjl", post, me)
# 부모 자체에 있는 클래스는 내용적인 의미가 있지 않기 때문에 =>

# 반드시 구체적인 자식 클래스로 쓴다.
# like = Like(post, me)
