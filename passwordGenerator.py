class Password_generate:

  def __init__(self) -> None:
    pass

  @staticmethod
  def password(old_password):

    print(".........password generator,.........\n\n")

    while True:

      user_password = input("Enter user password:....\n")

      # old_password = input("enter old password:....\n")

      if (user_password > "8"):

        if (user_password == old_password):
          print("password change successfully...\n\n\n")

          while True:
            new_password = input("Enter new password:....\n")

            confirm_password = input("Enter confirn password:,,.\n")
            password = new_password

            if (new_password == confirm_password):

              if ((new_password and confirm_password) >= "8"):
                print("password created successfylly...\n")
                print("........thank you.......\n")
                print("show the password,....\n") 
                
                print("password : " , password)

                
              else:
                print(
                    "password is not create bcz new password is not more then 8 charactor"
                )
                

            else:
              print("password invalide ....try agian\n")

            if (new_password == confirm_password):
              break

            else:
              continue

        else:
          print("invalide password:.....  \n")
          print("please try more again...\n")

      else:
        print(
            "password is not create bcz new password is not more then 8 charactor\n"
        )

        print("........thank you..../..")

      if (user_password == old_password):
        break

      else:
        continue


obj = Password_generate()
obj.password("bhoomi@1212")
