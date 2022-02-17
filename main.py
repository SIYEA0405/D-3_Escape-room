print("I woke up in a strange room.")
print('''
0================================================0
|'.                    (|)                     .'|
|  '.                   |                    .'  |
|    '.                |O|                 .'    |
|      '. ____________/===\_____________ .'      |
|        :            `\"/`  ______     :     .. |
|        :     mmmmmmm  V   |--%%--|    :   .'|| |
|        :     |  |  |      |-%%%%-|    :  |  || |
|        :     |--|--| @@@  |=_||_=|    :  I  || |
|        :     |__|__|@@@@@ |_\__/_|    :  |  || |
|        :             \|/   ____       :  |  || |
|        :;;       .'``(_)```\__/````:  :  |  || |
|        :||___   :================:'|  :  | 0+| |
|        :||===)  | |              | |  :  |  || |
|        ://``\\__|_|______________|_|__:  I  || |
|      .'/'    \' | '              | '   '.|  || |
|    .'           |                |       '. || |
|  .'                                        '|| |
|.'                                            '.|
0================================================0
''')
print("I have to escape from this room.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("There's a left door and a right door.\nGame over.")
door = input("Which door will you open? right or left\n").lower()

if door == "right":
  print("The door won't open\nGame over.")
elif door == "left":
  print('''
   _______________________________________________________________________________ 
|% % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % %| 
| % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % | 
|% % % % % %_____________________________ % % % % % % % % % % % % % % % % % % % | 
| % % % % %|  _________________________  | % % % % % % % % % % % % % % % % % % %| 
|% % _ % % |O|                         |O|% % % % % % % % % % _ % % % % % % % % | 
| % /_\ % %| | //                      | | % % % % % % % % % /_\ % % % % % % % %| 
|%  =|=  % |O|                         |O|% % % % % % % % %  =|=  % % % % % % % | 
| % % % % %| |    //                   | | % % % % % % % % % % % % % % % % % % %| 
|% % % % % |O|                         |O|% % % % % % % % % % % % % % % % % % % | 
|==========| |                         | |======================================| 
| SHOWERS  |O|                         |O|                                      | 
| <=====   | | //                      | |              ________________        | 
|          |O|_________________________|O|             |________________|       | 
|          |_____________________________|               |            |    _    | 
|           ______________/;____________                 |~           |  =)_)=  | 
|         /`        .--T--|--T--.       `\       ____    |            |   (_(   | 
|        /_________'------'------'________\     /PUSH\   |__%______%__|   )_)   | 
|         |  _____   ____   ____   _____ |     /______\   .`        `.          | 
|         | |__~__| |    | |    | |__~__||     |      |   :          :          | 
|         |         |    | |    |        |     |      |    '.      .'           | 
lc________|         |   {| |}   |        |_____|      |______\`'-'`/____________| 
          |         |    | |    |        |     |______|       |   | 
          |_________|____|_|____|________|                    |___| ''')
  print("It's the bathroom")
  bathroom = input("I can see the toilet. Should I flush it? Y or N\n").lower()
  if bathroom == "y":
    print("The key went down.\nGame over")
  elif bathroom == "n":
    print('''
   .--.
  /.-. '----------.
  \'-' .--"--""-"-'
   '--'' ''')
    print("I found the key!")
    use_key = input("Where are you going to put the key? Door or Window or Clock\n").lower()
    if use_key == "door":
      print("I heard the door open and the door exploded.\nGame over.")
    elif use_key == "window":
      print("I opened the window, but I couldn't get out.\nGame over.")
    elif use_key == "clock":
      print('''
        _____
     _.'_____`._
   .'.-'  12 `-.`.
  /,' 11      1 `.\
 // 10      /   2 \\
;;         /       ::
|| 9  ----O      3 ||
::                 ;;
 \\ 8           4 //
  \`. 7       5 ,'/
   '.`-.__6__.-'.'
    ((-._____.-))
    _))       ((_
   '--'       '--'
  ''')
      print("Time seemed to have stopped, but time began to reverse.\nI was able to come back before I was trapped like that.\n-You cleared it successfully-")
    else:
      print("I starved to death without doing anything.\nGame over.")
  else:
    print("It's a wrong command. Please refresh and try again")
else:
  print("It's a wrong command. Please refresh and try again")










