
r = 1
while r > 0:
    print(r)
    r = r - 1
    print("Inuti loopen")

print("Efter loopen")

user_input = ""
while user_input != "q":
    # user_input = input("Press 'q' to quit." + "\n< ")
    print("Press 'q' to quit.")
    user_input = input("< ")

print("Outside the loop.")


i = 0
while i < 3:
    print("Tre gånger: " + str(i))
    i = i + 1

print("----------------------")

for i in range(3):
    print("Tre gånger: " + str(i))