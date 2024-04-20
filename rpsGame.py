class RPS_Game:
  def __init__(self) -> None:
    pass
    
  @staticmethod
  def get_choices():
    
    print("Are you ready to play?")

    if(input("yes or no....") == "yes"):
    
      print("let's play,.....")
      print(input("enter username ......\n"))

        # choice = ['rock','paper','scissors']
      print("choice : 1. Rock\n 2. Paper\n 3. Scissors")
      while True:
         user1 = input("Enter first user .....\n")
         user2 = input("Enter second user .....\n")

         tie = 0

         if(user1 == user2): 
         
           print("ties")
           tie += 1
         elif (
           (user1 == 'rock' and user2 == 'scissors') 
           or (user1 == 'scissors' and user2 == 'rock')
         ):
          print("rock win....")

         elif (
           (user1 == 'paper' and user2 == 'scissors')
           or (user1 == 'scissors' and user2 == 'paper')):
          print("scissors win....")

         elif (
           (user1 == 'rock' and user2 == 'paper') or
               (user1 == 'paper' and user2 == 'rock')):
           
          print("rock win....")

         elif (tie == 3):
          print("game over")
           
         else:
          print("invalide choice....\n")

         print("can you play again game...... \n?")
        
         if (input("yes or no...") == 'no'):
             break
           
         else:
             continue
           
      print("thank you for playing this game ....take care")
      
    else:
        print("okay,.....")
      
  
   

G1 = RPS_Game()
G1.get_choices()
