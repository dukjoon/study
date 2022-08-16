# overriding, 자식이 부모를 거역

class Post:
    def comment(self, user, content):
        self.comments.append(Comment(user, content))

class ProtectedPost(Post):
    def comment(self, user, content):
        print("Can't comment on protected posts.")
        super().comment(user, content)