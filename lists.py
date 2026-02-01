
user_name = "Frodo"
friends = ["Sam", "Merry", "Pippin"]
print(user_name)
print(friends)
print(friends[-3])

friends.append("Sméagol")
friend_count = len(friends)
print("Number of friends: " + str(friend_count))
print(friends)
print(friends[-1])
print(friends[3])
print(friends[len(friends) - 1])
friends[-1] = "Gollum"
print(friends)
print(friends[-1])
friends.remove("Merry")
print(friends)
friends.pop()
print(friends)
