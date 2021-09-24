class User():

    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        self.followers=0
        self.following=0

    def follow(self,user):
        self.following+=1
        user.followers+=1

user1=User(9123,"Monalisa")
user2=User(9134,"Lindy")


print(user1.id)
print(user2.username)

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)

