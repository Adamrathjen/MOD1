class Character:
   
   
   
   def findName(name):
      flag = 0
      while flag != 1:
         name = input("Enter character name: ")
         if name == "Character" or "Name":
            print("That is not an acceptable name.")
         else:
            flag = 1
      return name
   


   def findDoor(door):
      choice = "4"
      while choice != "1" or "2" or "3":
         print("Do you choose to have allies(1)")
         print("Become skilled in anything(2)")
         print("Or to be separate from all others(3)")
         choice = input("Choose by selecting a number 1, 2, or 3")
         if choice == "1" or "2" or "3":
            door = choice
         else:
            print("Please choose 1, 2, or 3.")
      return door
         


   def findPedastle(pedastle):
      weapon = 5
      while weapon != "1" or "2" or "3" or "4":
         print("Do you choose to deal great damage(1)")
         print("Be able to defend against terrible foes(2)")
         print("Use magic for any circumstance(3)")
         print("Or inspire and strengthen others")
         weapon = input("Choose by selecting a number 1, 2, 3, or 4")
         if weapon == "1" or "2" or "3" or "4":
            pedastle = weapon
         else:
            print("Please choose 1, 2, 3, or 4.")
      return pedastle



   def findItem(item, pedastle):
      if pedastle == "1":
         item = input("Choose any weapon to weild:")
         return item
      elif pedastle == "2":
         item = input("Choose any armor to wear:")
         return item
      elif pedastle == "3":
         print("types of magic are: earth, fire, water, wind")
         print("lightning, mind, poison, light, dark")
         print("summoning, and celestial")
         item = input("Choose any magic to weild:")
         return item
      elif pedastle == "4":
         item = input("Choose any instrument to play:")
         return item



   def __init__(self, name, door, pedastle, item):
      self.name = findName(name)
      self.door = findDoor(door)
      pedastle = findPedastle(pedastle)
      self.pedastle = pedastle
      self.item = findItem(item, pedastle)