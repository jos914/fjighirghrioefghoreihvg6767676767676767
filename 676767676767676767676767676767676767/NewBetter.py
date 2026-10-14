print("Welcome")
print("You are stuck on an island inside a small hut")

a1 = input("Do you walk out the door or jump out the window? ").lower()

if a1 == "door":
    print("You walk out the door and see two men")
    print("They kidnap you and sell you on the black market")
    print("Game Over")

elif a1 == "window":
    print("You walk out the window and in front of you is a forest and an open plain")
    a2 = input("Do you go into the plain or the forest? ").lower()

    if a2 == "forest":
        print("You walk into the forest and you see monkeys with machine guns")
        print("They shoot you with their guns and eventually toss you to the moon")
        print("Game Over")

    elif a2 == "plain":
        print("You walk through the plain and you come across a beach and another forest")
        a3 = input("Do you go into the forest or onto the beach? ").lower()

        if a3 == "beach":
            print("You walk onto the beach and you see two men who tie you up")
            print("They eventually auction you out at a sketchy street mall on another island")
            print("Game Over")

        elif a3 == "forest":
            print("You walk through the plain and you come across a beach and a cave")
            a4 = input("Do you go into the cave or onto the beach? ").lower()

            if a4 == "beach":
                print("You walk onto the beach and you see two men who tie you up")
                print("They eventually auction you out at a sketchy street mall on another island")
                print("Game Over")

            elif a4 == "cave":
                print("You walk into the cave and you find a teleporter")
                print("You also see two men in the cave standing next to the teleporter")
                print("You see a mirror image of yourself in a corner")
                print("The two men are talking about an auction price")
                print("Before they find you, you run into the teleporter and you are teleported to another island")

            else:
                print("Invalid choice")

        else:
            print("Invalid choice")

    else:
        print("Invalid choice")

else:
    print("Invalid choice")
