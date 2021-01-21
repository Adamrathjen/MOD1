import os
print("Character Creator!")

selected = 1
while "4" != selected:
    print("Make new Character: 1")
    print("Delete character: 2")
    print("See current characters: 3")
    print("Quit: 4")


    selected = input("Make your selection: ")
    if selected == "1": 
        print("you selected 1")
        characterName = input("Enter a character name: ")
        f = open(characterName, "x")

        print("make character and create character file function call") 
    elif selected == "2": 
        print("you selected 2")
        filename = input("Enter the name of the character to delete or enter n to stop: ")
        if filename != "n":
            if os.path.exists(filename):
                os.remove(filename)
            else:
                print("The file does not exist")
        else: continue
    elif selected == "3": 
        print("you selected 3")
        print("function call to display list of created characters")
    elif selected == "4": 
        print("you quit")
    else: 
        print("that isn't an option")

print("you got out")