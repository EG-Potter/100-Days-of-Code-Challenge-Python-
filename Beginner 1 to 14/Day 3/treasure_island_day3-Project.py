print('''
       _                                     _     _                 _ 
      | |                                   (_)   | |               | |
      | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
      | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
      | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
       \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|


      ____________________________________________________________________
     |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
     |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
     | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
     |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
     |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
     |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
     |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
     |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
     | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
     |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
     |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
     | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
     |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
     | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
     |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
     | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
     |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
     | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
     |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
     |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

option1 = input("Left or Right?\n")

if option1.lower() == "left":
    option2= input("Swim or Wait?\n")
    if option2.lower() == "wait":
        option3 = input("Which door?\n")
        if option3.lower() == "red":
            print("Burned by fire. Game Over")
        elif option3.lower() == "blue":
            print("Eaten by beasts, Game Over")
        elif option3.lower() == "yellow":
            print("You Win")
        else:
            print("Game Over")
    else:
        print("Attacked by trout. Game Over")
else:
  print("Fall into a hole. Game Over")