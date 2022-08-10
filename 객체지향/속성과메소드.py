class Post:
    def like(self, user):
        self.liked_users.append(user)

    def num_likes(self):
        return len(self.liked_users)
