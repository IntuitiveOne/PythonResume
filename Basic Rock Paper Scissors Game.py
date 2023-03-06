def main():
    import random

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____) rock
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______) paper
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________) scissors
          (____)
    ---.__(___)
    '''

    game_images = [rock, paper, scissors]   #putting text art into an easy to access list to ouput appropiate image with results of user input and computer choice

    weapon = input("\nWelcome to the Rock, Paper, Scissors Game\nChoose your weapon - Type 0 for Rock, 1 for Paper or 2 for Scissors\n\n")

    weapon = int(weapon)
    weaponai = random.randint(0,2)          #randomize computers choice

    if weapon in range(-1, 3):              #range to make sure user has selected an appropiate input
        print("\nEngaging in Combat")
    

        if weapon == weaponai:
            print("\nThe computer matched your weapon choice of "+game_images[weapon]+"\nit is a draw!")
        elif weapon == 2 and weaponai == 0:
                print("\nYou chose "+game_images[weapon]+" \nand the computer chose "+game_images[weaponai]+"\nyou lost!")
        elif weapon == 0 and weaponai == 2:
                    print("\nYou chose "+game_images[weapon]+" \nand the computer chose "+game_images[weaponai]+"\nyou won!")
        elif weapon > weaponai:
                        print("\nYou chose "+game_images[weapon]+" \nand the computer chose "+game_images[weaponai]+"\nyou won!")
        elif weapon < weaponai:
                            print("\nYou chose "+game_images[weapon]+" \nand the computer chose "+game_images[weaponai]+"\nyou lost!")
    else:
            print("Your weapon choice is not available, choose again")
            

    line = input("\nPlay again (Y/N)?\n\n")  #basic play again function, could use a while loop to repeat asking user for an input until a no or yes is given, decided not to due to simplicity of the program

    if line.casefold() == "y":
        main()

    else:
        exit()        

main() 